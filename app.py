import streamlit as st

st.set_page_config(
    page_title="AgroGPT",
    page_icon="🌱",
    layout="wide",
)

# ---------------- CSS ----------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#0f172a;
}

[data-testid="stHeader"]{
    background:transparent;
}

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

.hero{
    background:linear-gradient(90deg,#0f5132,#198754);
    border-radius:18px;
    padding:35px;
    color:white;
    margin-bottom:25px;
}

.card{
    background:#1e293b;
    padding:25px;
    border-radius:18px;
    text-align:center;
    border:1px solid #2dd4bf;
}

.card h2{
    color:white;
}

.card h1{
    color:#4ade80;
}

.feature{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero ----------------

st.markdown("""
<div class="hero">

# 🌾 AgroGPT

### AI Agriculture Assistant

Upload Agriculture PDFs, Build a Knowledge Base and Chat with your Documents using AI.

</div>
""", unsafe_allow_html=True)

# ---------------- Dashboard ----------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
<div class="card">
<h1>📄</h1>
<h2>Documents</h2>
<h1>4</h1>
</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<h1>🤖</h1>
<h2>LLM</h2>
<h3>Gemini Flash</h3>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<h1>🧠</h1>
<h2>Embedding</h2>
<h3>MiniLM</h3>
</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="card">
<h1>💾</h1>
<h2>Vector DB</h2>
<h3>FAISS</h3>
</div>
""",unsafe_allow_html=True)

st.write("")

# ---------------- Workflow ----------------

st.subheader("🚀 Workflow")

st.success("1️⃣ Upload Agriculture PDFs")

st.success("2️⃣ Build Knowledge Base")

st.success("3️⃣ Open Chat")

st.success("4️⃣ Ask Questions")

st.success("5️⃣ Get AI-powered Answers")

st.divider()

# ---------------- Features ----------------

st.subheader("✨ Features")

col1,col2=st.columns(2)

with col1:

    st.markdown("""
<div class="feature">

### 📄 Upload Documents

Upload multiple Agriculture PDFs.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="feature">

### 📚 Knowledge Base

Automatically build a searchable AI knowledge base.

</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature">

### 💬 AI Chat

Ask questions in natural language.

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="feature">

### ⚡ RAG Powered

LangChain + Gemini + FAISS + MiniLM

</div>
""",unsafe_allow_html=True)

st.divider()

# ---------------- Quick Navigation ----------------

st.subheader("📌 Navigation")

st.info("""
🏠 Home

💬 Chat

📤 Upload

📚 Knowledge Base

📊 Analytics

ℹ️ About
""")

# ---------------- Footer ----------------

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit | LangChain | Gemini | FAISS | HuggingFace

</div>
""",unsafe_allow_html=True)


