from src.loader import load_documents
from src.text_splitter import split_documents

docs = load_documents()
chunks = split_documents(docs)

print("\nFirst Chunk:\n")
print(chunks[0].page_content)