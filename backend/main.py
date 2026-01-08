# # # from fastapi import FastAPI, UploadFile, File
# # # from document_loader import load_pdf
# # # from rag import build_rag
# # # import shutil

# # # app = FastAPI()

# # # vectorstore = None
# # # llm = None

# # # @app.post("/upload")
# # # async def upload_file(file: UploadFile = File(...)):
# # #     global vectorstore, llm
# # #     file_path = f"temp_{file.filename}"

# # #     with open(file_path, "wb") as buffer:
# # #         shutil.copyfileobj(file.file, buffer)

# # #     text = load_pdf(file_path)
# # #     vectorstore, llm = build_rag(text)

# # #     return {"message": "Document indexed successfully"}

# # # @app.post("/ask")
# # # async def ask(query: str):
# # #     retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
# # #     docs = retriever.get_relevant_documents(query)

# # #     context = "\n".join([d.page_content for d in docs])

# # #     prompt = f"""
# # #     You are a professional career coach.
# # #     Use ONLY the information below:

# # #     {context}

# # #     Question: {query}
# # #     """

# # #     response = llm.invoke(prompt)
# # #     return {"answer": response.content}









# # from fastapi import FastAPI, UploadFile, File
# # from document_loader import load_pdf
# # from rag import build_rag
# # import shutil
# # import traceback

# # app = FastAPI()

# # vectorstore = None
# # llm = None

# # @app.post("/upload")
# # async def upload_file(file: UploadFile = File(...)):
# #     global vectorstore, llm
# #     try:
# #         file_path = f"temp_{file.filename}"

# #         with open(file_path, "wb") as buffer:
# #             shutil.copyfileobj(file.file, buffer)

# #         text = load_pdf(file_path)
# #         vectorstore, llm = build_rag(text)

# #         return {"message": "Document indexed successfully"}

# #     except Exception as e:
# #         return {
# #             "error": str(e),
# #             "traceback": traceback.format_exc()
# #         }
    





# from fastapi import FastAPI, UploadFile, File
# from pydantic import BaseModel
# import shutil
# import traceback

# # Assume these are your RAG helpers
# from document_loader import load_pdf  # function to extract text from PDF
# from rag import build_rag           # function to build vectorstore and LLM

# app = FastAPI()

# # Globals to store vectorstore and LLM instance
# vectorstore = None
# llm = None

# # -----------------------------
# # POST /upload : Upload PDF & Index
# # -----------------------------
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     global vectorstore, llm
#     try:
#         # Save the uploaded file temporarily
#         file_path = f"temp_{file.filename}"
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         # Load PDF text
#         text = load_pdf(file_path)

#         # Build vectorstore and LLM (RAG setup)
#         vectorstore, llm = build_rag(text)

#         return {"message": "Document indexed successfully"}

#     except Exception as e:
#         return {
#             "error": str(e),
#             "traceback": traceback.format_exc()
#         }

# # -----------------------------
# # POST /ask : Ask a question
# # -----------------------------
# class Question(BaseModel):
#     question: str

# @app.post("/ask")
# async def ask_question(q: Question):
#     global vectorstore, llm

#     if vectorstore is None or llm is None:
#         return {"error": "No document indexed yet. Upload a PDF first."}

#     try:
#         # Retrieve top 3 relevant chunks from the PDF
#         docs = vectorstore.similarity_search(q.question, k=3)
#         context = " ".join([doc.page_content for doc in docs])

#         # Generate answer using your LLM
#         answer = llm(f"Context: {context}\nQuestion: {q.question}")

#         return {"answer": answer}

#     except Exception as e:
#         return {
#             "error": str(e),
#             "traceback": traceback.format_exc()
#         }
            

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import traceback

# RAG helpers
from document_loader import load_pdf  # PDF text extraction
from rag import build_rag           # Build vectorstore & LLM
from langchain_core.messages import HumanMessage  # For ChatGoogleGenerativeAI

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 IDI IKKADA ADD CHEYYALI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # frontend anywhere nundi allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Globals
vectorstore = None
llm = None

# -----------------------------
# POST /upload : Upload PDF & Index
# -----------------------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global vectorstore, llm
    try:
        # Save uploaded PDF temporarily
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text from PDF
        text = load_pdf(file_path)

        # Build RAG: vectorstore + LLM
        vectorstore, llm = build_rag(text)

        return {"message": "Document indexed successfully"}

    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }

# -----------------------------
# POST /ask : Ask a question
# -----------------------------
class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Question):
    global vectorstore, llm

    if vectorstore is None or llm is None:
        return {"error": "No document indexed yet. Upload a PDF first."}

    try:
        # Get top 3 relevant chunks
        docs = vectorstore.similarity_search(q.question, k=3)
        context = " ".join([doc.page_content for doc in docs])

        # Generate answer using ChatGoogleGenerativeAI
        answer_obj = llm.generate([[HumanMessage(content=f"Context: {context}\nQuestion: {q.question}")]])
        answer = answer_obj.generations[0][0].text

        return {"answer": answer}

    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
