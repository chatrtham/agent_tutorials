import os
from dotenv import load_dotenv

# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_fireworks import ChatFireworks
# from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Initialize LLM
# LLM = ChatGroq(model="llama-3.2-90b-text-preview",
#                     temperature=0)

# LLM = ChatOpenAI(model="gpt-4o-2024-08-06",
#                         temperature=0)


LLM = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-002",
    temperature=0,
    )


# FIREWORKS_LLM = ChatFireworks(model="accounts/fireworks/models/llama-v3-70b-instruct")

# OLLAMA_LLM = ChatOllama(model="llama3.1",
#                         temperature=0,
#                         # format="json"
#                         )
