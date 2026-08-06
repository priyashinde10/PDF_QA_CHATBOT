# ==========================================================
# chatbot.py
# Main Chatbot Logic
# ==========================================================

from rag import load_vector_store
from utils.qa import generate_answer


class PDFChatBot:

    def __init__(self):
        self.db = load_vector_store()

    def ask(self, question):

        # Retrieve top 3 relevant chunks
        docs = self.db.similarity_search(question, k=3)

        # Combine chunks into context
        context = "\n\n".join([doc.page_content for doc in docs])

        # Generate answer using Ollama
        answer = generate_answer(question, context)

        return answer, docs