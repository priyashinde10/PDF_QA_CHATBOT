# ==========================================================
# qa.py
# Question Answering using Ollama (Llama 3.2)
# ==========================================================

from langchain_ollama import ChatOllama

# Load Llama 3.2
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def generate_answer(question, context):

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the given context.

If the answer is not found in the context, reply exactly:

I could not find the answer in the uploaded PDF.

Keep the answer short (3 to 5 sentences).

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content