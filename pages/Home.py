import streamlit as st

st.set_page_config(
    page_title="AgroGPT",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgroGPT")

st.subheader("AI Agriculture Assistant")

st.write(
    """
Welcome to **AgroGPT**, an AI-powered Agriculture Assistant.

This application allows you to:

✅ Upload Agriculture PDFs

✅ Create a Knowledge Base

✅ Ask Questions using AI

✅ Get Accurate Answers from your documents

✅ Manage Multiple Agriculture Documents
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.success("📄 Upload PDFs")

with col2:
    st.info("📚 Build Knowledge Base")

with col3:
    st.warning("🤖 Chat with AI")

st.divider()

st.header("Workflow")

st.markdown("""
1. Upload PDF
2. Create Knowledge Base
3. Open Chat
4. Ask Questions
5. Get Answers
""")