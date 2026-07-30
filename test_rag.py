from src.rag_pipeline import ask_question

question = input("Ask your question: ")

answer = ask_question(question)

print("\nAgroGPT:\n")
print(answer)