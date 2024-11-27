FROM python:3.11-slim

RUN pip install streamlit streamlit-chat langchain langchain-community langsmith langchain-google-genai faiss-cpu pypdf python-dotenv sentence-transformers

CMD ["streamlit", "run", "rag/main.py"]
