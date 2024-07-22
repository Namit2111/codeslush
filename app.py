from flask import Flask, render_template, request, jsonify
from utils import yt_trsndcrpt , gemini,embeddings,git
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarizer')
def summarizer():
    return render_template('summarizer.html')

@app.route('/chatpdf')
def chatpdf():
    return render_template('chatpdf.html')

@app.route('/github')
def github():
    return render_template('github.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    link = request.form.get('link')
    transcript = yt_trsndcrpt.get_transcript(link)
    prompt = f"Summarize the following transcript generate most importatn points, summary and points to be notes and also wrap headings in h1 tag: {transcript}"
    summary = gemini.chat(prompt)
    # Replace with actual summarization logic
    return jsonify({'summary': summary})

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    file = request.files.get('pdf')
    file.save(file.filename)
    documents = embeddings.load_pdf(filename=file.filename)
    document_list,embeddings_list,ids_list,metadata_list = embeddings.create_embeddings(documents)
    chroma_client = embeddings.initialize_chromadb()
    collection = embeddings.get_or_create_collection(chroma_client)
    embeddings.store_embeddings(collection,document_list,embeddings_list,ids_list,metadata_list)
    # Replace with actual PDF processing logic
    response = 'PDF uploaded successfully. Ready to chat.'
    return jsonify({'response': response})

@app.route('/chat_pdf', methods=['POST'])
def chat_pdf():
    message = request.form.get('message')
    collection = embeddings.get_or_create_collection(embeddings.initialize_chromadb())
    context = embeddings.search_embeddings(collection,message)
    # print(context)
    prompt = f" based on context of pdf asnwer the question if qestion is not present in the context then dont answer.  context : {context['documents'][0][0]} \n\n question : {message}  "
    response = gemini.chat(prompt)
    return jsonify({'response': response})

@app.route('/github_repo', methods=['POST'])
def github_repo():
    repo_link = request.form.get('repo_link')
    global code 
    code = git.get_python_code_from_repo(repo_link,clone_path='repo')
    # code = f'Code from {repo_link}: This is dummy code content.'
    return jsonify({'code': code})

@app.route('/chat_github', methods=['POST'])
def chat_github():
    message = request.form.get('message')
    prompt = f" based on context of github repository asnwer the question if qestion is not present in the context then dont answer.  context : {code} \n\n question : {message}  "
    response = gemini.chat(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
