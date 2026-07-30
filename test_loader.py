from src.loader import load_documents

documents = load_documents()

print("\nFirst Page:\n")
print(documents[0].page_content[:500])