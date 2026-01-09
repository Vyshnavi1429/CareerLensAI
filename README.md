# CareerLens AI – Resume Intelligence Chat

A single-user GenAI web application that analyzes resumes using Retrieval Augmented Generation (RAG) to provide career guidance, skill gap analysis, and personalized recommendations.

![Backend](https://img.shields.io/badge/Backend-FastAPI-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%2B%20JS-purple)
![VectorDB](https://img.shields.io/badge/VectorDB-FAISS-orange)
![LLM](https://img.shields.io/badge/LLM-Gemini-green)

## Features

- 📄 **Resume Upload**: Upload PDF resumes for intelligent analysis
- 🧠 **RAG Architecture**: Retrieval Augmented Generation for grounded responses
- 🔍 **Semantic Search**: FAISS vector search over resume chunks
- 🧩 **Local Embeddings**: Sentence Transformers (no paid embedding APIs)
- ✨ **Gemini LLM**: Google Gemini for accurate, contextual answers
- 💬 **Resume-aware Chat**: Ask questions strictly based on resume content
- 🎨 **Modern UI**: Clean and responsive frontend interface
- 🚀 **FastAPI Backend**: High-performance Python API

## Tech Stack

### Backend
- **FastAPI** – REST API framework
- **LangChain** – RAG pipeline
- **FAISS** – Vector similarity search
- **sentence-transformers** – Local embeddings
- **Google Generative AI (Gemini)** – LLM
- **pdfplumber** – PDF text extraction
- **Uvicorn** – ASGI server

### Frontend
- **HTML + CSS** – UI
- **Vanilla JavaScript** – API integration
- **Fetch API** – Backend communication

## Project Structure

career-coach-ai/
│
├── backend/
│ ├── main.py
│ ├── rag.py
│ ├── document_loader.py
│ ├── requirements.txt
│ └── .env
│
├── frontend/
│ └── index.html
│
└── README.md


## Setup Instructions

### Prerequisites

- Python 3.10+
- Git
- Google Gemini API Key

### Backend Setup

git clone https://github.com/your-username/career-coach-ai.git
cd career-coach-ai

python -m venv venv

### Activate virtual environment:

Windows (PowerShell):

venv\Scripts\activate

If activation is blocked:

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

### Install dependencies:

cd backend
pip install -r requirements.txt

If required, install embeddings manually:

pip install sentence-transformers

Create a .env file inside backend:

GOOGLE_API_KEY=your_gemini_api_key_here

### Start the backend server:

uvicorn main:app --reload

### Backend runs at:

http://127.0.0.1:8000

### Swagger Docs:

http://127.0.0.1:8000/docs

### Frontend Setup
Open the frontend file directly:

frontend/index.html

Ensure backend URL is set correctly in JavaScript:

const API = "http://127.0.0.1:8000";

### Usage
Upload a PDF resume

Wait for indexing to complete

View suggested skills to improve and develop

Ask career-related questions in chat

Get answers strictly based on resume data

### API Endpoints
Endpoint	Method	Description
/upload	POST	Upload and index resume
/ask	POST	Ask resume-based questions

### RAG Workflow
Resume PDF is uploaded

Text is extracted and chunked

Embeddings are generated locally

FAISS stores vector representations

User queries retrieve relevant chunks

Gemini generates grounded responses

### Notes
Only PDF resumes are supported

No hallucinations – answers are strictly resume-based

First run downloads embedding model (~90MB)

Designed for academic and demo use

### Git Push Steps
git add .
git commit -m "Initial CareerLens AI project"
git push origin main
License
MIT – Educational Use Only

### Team
GEN AI TEAM 19
K.S.S.L. Khechar
Sk. Zainab
M. Vyshnavi
P. Akhila
Y. Sathish
K. Nihar
K. Vishnuvardhan
