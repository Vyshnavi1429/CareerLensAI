from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

def build_rag(text):
    # 1. Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # 2. LOCAL embeddings (NO API, NO QUOTA)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 3. Vector store
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # 4. Gemini LLM (ONLY for generation)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    return vectorstore, llm
