from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from chromadb.config import Settings
import uuid
def load_pdf(filename):
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    documents = text_splitter.split_documents(pages)

    return documents



def create_embeddings(documents,filename = "test"):
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    document_list = []
    embeddings_list = []
    ids_list = []
    metadata_list = []
    for i,doc in enumerate(documents):
        embedding = embeddings_model.embed_query(doc.page_content)
        # document_embeddings.append({
        #     'text': doc.page_content,
        #     'embedding': embedding
        # })
        document_list.append(doc.page_content)
        embeddings_list.append(embedding)
        ids_list.append(f"{filename}_{i}")
        metadata_list.append(doc.metadata)
    return document_list,embeddings_list,ids_list,metadata_list


    

def search_embeddings(collection, query):
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    query_embedding = embeddings_model.embed_query(query)
    results = collection.query(query_embeddings=query_embedding, n_results=2,include=["documents","metadatas"])
    return results


def initialize_chromadb():
    """Initialize the ChromaDB client."""
    # settings = Settings()  # Ensure only valid fields are passed
    # chroma_client = chromadb.Client(settings)
    client = chromadb.PersistentClient(path="./test")
    return client

def get_or_create_collection(chroma_client, collection_name="document_embeddings"):
    """Get or create a collection in ChromaDB."""
    # if collection_name not in chroma_client.list_collections():
    #     collection = chroma_client.create_collection(collection_name)
    # else:
    #     collection = chroma_client.get_collection(collection_name)
    collection = chroma_client.get_or_create_collection(
        name=collection_name
    )
    return collection

def store_embeddings(collection, document_list,embeddings_list,ids_list,metadata_list):
    """Store the document embeddings in ChromaDB."""
    collection.add(
        ids=ids_list,
        documents=document_list,
        embeddings=embeddings_list,
        metadatas=metadata_list
    )