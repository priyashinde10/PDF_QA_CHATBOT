# ==========================================================
# rag.py
# Build and Load FAISS Vector Store
# ==========================================================

from langchain_community.vectorstores import FAISS

from utils.loader import load_pdfs
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model


def create_vector_store():

    print("\nLoading PDFs...")

    documents = load_pdfs()

    print(f"Pages Loaded : {len(documents)}")

    print("\nSplitting Documents...")

    chunks = split_documents(documents)

    print(f"Chunks Created : {len(chunks)}")

    print("\nCreating FAISS Index...")

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local("vector_db")

    print("\nFAISS Database Created Successfully!")

    return vector_store


def load_vector_store():

    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store