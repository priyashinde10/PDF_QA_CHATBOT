# ==========================================================
# splitter.py
# Split PDF into smaller text chunks
# ==========================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split PDF documents into smaller chunks.

    Returns:
        list[Document]
    """

    text_splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    )

    chunks = text_splitter.split_documents(documents)

    return chunks