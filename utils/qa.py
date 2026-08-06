import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
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

    return response.text