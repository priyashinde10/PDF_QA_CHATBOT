# ==========================================================
# retriever.py
# FAISS Retriever
# ==========================================================

from rag import VectorStoreManager


class Retriever:

    def __init__(self):

        manager = VectorStoreManager()

        self.db = manager.load_vector_store()

    def retrieve(self, question, k=3):
        """
        Retrieve top-k relevant chunks.
        """

        docs = self.db.similarity_search(
            question,
            k=k
        )

        return docs