### README

# Flask App with Summarization, PDF Chat, and GitHub Analysis

This Flask web application provides a set of utilities for interacting with YouTube transcripts, PDFs, and GitHub repositories. It leverages AI to summarize content, chat with PDF documents, and analyze code from GitHub repositories.

## Features

- **YouTube Transcript Summarization**: Summarize YouTube video transcripts with important points and headings.
- **Chat with PDF**: Upload a PDF, create embeddings, and chat with the document by asking questions based on its content.
- **GitHub Repository Analysis**: Extract Python code from a GitHub repository and interact with it using AI.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage

1. **Access the application**: Open your browser and go to `http://127.0.0.1:5000/`.
2. **YouTube Transcript Summarization**:
   - Navigate to `/summarizer`.
   - Enter a YouTube video link and receive a summarized transcript.
3. **Chat with PDF**:
   - Navigate to `/chatpdf`.
   - Upload a PDF and start asking questions about its content.
4. **GitHub Repository Analysis**:
   - Navigate to `/github`.
   - Enter a GitHub repository link, extract Python code, and interact with the codebase.

## API Endpoints

- `/summarize`: POST endpoint to summarize a YouTube video transcript.
- `/upload_pdf`: POST endpoint to upload and process a PDF.
- `/chat_pdf`: POST endpoint to chat with a processed PDF.
- `/github_repo`: POST endpoint to extract Python code from a GitHub repository.
- `/chat_github`: POST endpoint to chat with the extracted code from a GitHub repository.

## Dependencies

- Flask
- `yt_trsndcrpt`: A utility for getting YouTube transcripts.
- `gemini`: An AI model for generating responses.
- `embeddings`: A utility for handling PDF embeddings and interactions.
- `git`: A utility for interacting with GitHub repositories.

