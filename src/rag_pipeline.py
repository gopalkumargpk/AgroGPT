from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

from src.llm import get_llm
from src.retriever import get_retriever


def ask_question(question: str):

    llm = get_llm()
    retriever = get_retriever()

    # Retrieve documents
    docs = retriever.get_relevant_documents(question)

    # Debug Information
    st.subheader("📄 Debug Information")
    st.write("Retrieved Documents:", len(docs))

    for i, doc in enumerate(docs, start=1):
        st.write(f"### Document {i}")
        st.write("Source:", doc.metadata.get("source", "Unknown"))
        st.write(doc.page_content[:500])

    # No documents found
    if not docs:
        return "I couldn't find any relevant information in the uploaded agriculture documents."

    # Build context
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_template(
        """
You are AgroGPT, an AI Agriculture Assistant.

Answer ONLY from the context below.

Rules:
- Give clear answers.
- If the answer exists in the context, answer it.
- Do not invent information.
- If the answer is not in the context, reply exactly:

I couldn't find the answer in the uploaded agriculture documents.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response.content