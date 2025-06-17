import os
import streamlit as st
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from langchain_community.chat_models import ChatOllama 

# Optional: ตั้งค่า base_url หาก Ollama รันใน Docker network
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")  # หรือ "http://localhost:11434" ถ้ารันนอก container

# Define the LLM using Ollama
llm = ChatOllama(
    model="gemma:2b",  # 👈 ชื่อโมเดลที่คุณได้ pull เช่น `llama3`, `llama3:8b`
    base_url=OLLAMA_BASE_URL,
    temperature=0.0,
    streaming=True,
)

# Define the embedding model (same)
embeddings = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
