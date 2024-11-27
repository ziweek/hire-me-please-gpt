from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st

def get_embeddings_gemini():
    embeddings_genai = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=st.secrets["GOOGLE_API_KEY"]
    )
    return embeddings_genai
