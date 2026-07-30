from src.llm import get_llm

llm = get_llm()

response = llm.invoke("Hello! Introduce yourself in one sentence.")

print(response.content)