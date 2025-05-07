from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()  # Ensures the GROQ_API_KEY is loaded

def load_llm(model_name="llama3-8b-8192"):
    return ChatGroq(
        model_name=model_name,
        temperature=0.7,  # Adjust for creativity
    )
llm = load_llm()
print(llm.invoke("What is the best practice for Python list comprehensions?"))
