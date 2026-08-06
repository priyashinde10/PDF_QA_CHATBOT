import os
import shutil
import streamlit as st

from chatbot import PDFChatBot
from rag import create_vector_store

# ----------------------------------------------------

st.set_page_config(
    page_title="PDF Question Answering Chatbot",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#f4f7fb;
}

/* Header */
.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1E3A8A;
    margin-bottom:0px;
}

.subtitle{
    font-size:18px;
    color:#6B7280;
    margin-top:-10px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#1E3A8A,#3B82F6);
    color:white;
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] span {
    color: white;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.12);
    padding: 15px;
    border-radius: 15px;
    border: 2px dashed white;
}
/* Dashboard Cards */
.metric-card{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0px 6px 18px rgba(0,0,0,.08);
    text-align:center;
    transition:.3s;
}

.metric-card:hover{
    transform:translateY(-5px);
}

/* Answer Box */
.answer-box{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 18px rgba(0,0,0,.08);
}

/* Source Box */
.source-box{
    background:#ffffff;
    border-radius:15px;
    padding:18px;
    margin-bottom:12px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}

/* Button */

.stButton>button{

    width:100%;

    border-radius:12px;

    background:#2563EB;

    color:white;

    height:50px;

    font-size:18px;

    border:none;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* Text Input */

.stTextInput>div>div>input{

    border-radius:12px;

    border:2px solid #2563EB;

}
/* Fix Browse Files Button */
[data-testid="stFileUploader"] button {
    background-color: white !important;
    color: #1E3A8A !important;
    border: 2px solid #1E3A8A !important;
    border-radius: 10px !important;
    font-weight: bold !important;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #1E3A8A !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<h1 style='text-align:center;
color:#2563EB;
font-size:48px;
margin-bottom:5px;'>
🤖 PDF AI Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;
font-size:20px;
color:gray;
margin-top:0px;'>
Ask intelligent questions from multiple PDF documents using
<b>LangChain + FAISS + Llama 3.2</b>
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("📂 Document Manager")

st.sidebar.markdown("---")

st.sidebar.write(
    "Upload one or more PDF files."
)

st.sidebar.info(
    "After uploading, click **Process PDFs**."
)

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF files",
    type="pdf",
    accept_multiple_files=True
)

# ==========================================================
# DASHBOARD
# ==========================================================

pdf_count = len(uploaded_files) if uploaded_files else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📄 PDFs Uploaded",
        pdf_count
    )

with col2:
    st.metric(
        "🤖 AI Model",
        "Llama3.2"
    )

with col3:
    st.metric(
        "🧠 Embeddings",
        "MiniLM"
    )

with col4:
    st.metric(
        "📚 Vector DB",
        "FAISS"
    )

st.markdown("---")


# ----------------------------------------------------

if st.sidebar.button("📚 Process PDFs"):

    if not uploaded_files:
        st.sidebar.warning("Please upload at least one PDF.")
    else:

        # Remove old PDFs
        if os.path.exists("pdfs"):
            shutil.rmtree("pdfs")

        os.makedirs("pdfs")

        # Save uploaded PDFs
        for pdf in uploaded_files:

            with open(
                os.path.join("pdfs", pdf.name),
                "wb"
            ) as f:

                f.write(pdf.getbuffer())

        # Remove old vector database
        if os.path.exists("vector_db"):
            shutil.rmtree("vector_db")

        with st.spinner(
            "📄 Reading PDFs...\n\n🧠 Creating embeddings...\n\n📚 Building vector database..."
        ):

            create_vector_store()

        st.session_state.bot = PDFChatBot()

        st.sidebar.success("✅ PDFs processed successfully!")

        st.balloons()

# ----------------------------------------------------

if "bot" not in st.session_state:
    st.info("Upload PDFs and click 'Process PDFs' first.")
    st.stop()

bot = st.session_state.bot
# ==========================
# Initialize Chat History
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# Show Previous Messages
# ==========================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            if "sources" in message:

                with st.expander("📚 Sources"):

                    for doc in message["sources"]:

                        st.markdown(f"""
**📄 {doc.metadata.get('pdf_name')}**

**Page:** {doc.metadata.get('page') + 1}

---

{doc.page_content}

---
""")


# ==========================
# Chat Input
# ==========================

prompt = st.chat_input("Ask anything about your PDFs...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate answer
    with st.spinner("Searching PDFs..."):
        answer, docs = bot.ask(prompt)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": docs
        }
    )

    # Refresh the page
    st.rerun()