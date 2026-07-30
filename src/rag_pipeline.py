from langchain_core.prompts import ChatPromptTemplate

from src.llm import get_llm
from src.retriever import get_retriever


def ask_question(question: str):

    llm = get_llm()
    retriever = get_retriever()

    docs = retriever.invoke(question)

    print("\n========== RETRIEVED DOCUMENTS ==========\n")

    for i, doc in enumerate(docs, start=1):
        print(f"\n----------- Document {i} -----------")
        print("Source:", doc.metadata.get("source", "Unknown"))
        print(doc.page_content[:500])

    print("\n=========================================\n")

    if not docs:
        return "I couldn't find any relevant information in the uploaded agriculture documents."

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