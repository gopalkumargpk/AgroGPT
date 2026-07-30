from langchain_community.vectorstores import FAISS

from src.loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import get_embedding_model
from src.config import FAISS_PATH


def create_vector_store():
    """
    Create and save the FAISS vector database.
    """

    print("📄 Loading documents...")
    documents = load_documents()

    print("✂️ Splitting documents...")
    chunks = split_documents(documents)

    print("🧠 Creating embeddings...")
    embedding_model = get_embedding_model()

    print("💾 Creating FAISS index...")
    vector_db = FAISS.from_documents(chunks, embedding_model)

    vector_db.save_local(FAISS_PATH)

    print(f"✅ Vector database saved at: {FAISS_PATH}")


if __name__ == "__main__":
    create_vector_store()