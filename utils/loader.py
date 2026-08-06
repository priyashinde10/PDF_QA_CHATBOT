# ==========================================================
# loader.py
# Load Multiple PDF Documents
# ==========================================================

import os

from langchain_community.document_loaders import PyPDFLoader


def load_pdfs(folder_path="pdfs"):

    documents = []

    # Get all PDF files
    pdf_files = [
        file for file in os.listdir(folder_path)
        if file.endswith(".pdf")
    ]

    if not pdf_files:
        raise Exception("No PDF files found.")

    # Load every PDF
    for pdf in pdf_files:

        pdf_path = os.path.join(folder_path, pdf)

        print(f"Loading PDF: {pdf}")

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        # Add PDF filename to metadata
        for doc in docs:
            doc.metadata["pdf_name"] = pdf

        documents.extend(docs)

    return documents