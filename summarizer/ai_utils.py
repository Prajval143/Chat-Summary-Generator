from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:latest")

prompt = PromptTemplate(
    input_variables=["chat"],
    template="Summarize the following chat in one sentence:\n\n{chat}"
)

chain = prompt | llm


def summarize_chat(chat):
    conversation = "\n".join([f"{m['role'].capitalize()}: {m['message']}" for m in chat])
    result = chain.invoke({"chat": conversation})
    return result



