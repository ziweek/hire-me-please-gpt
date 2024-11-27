from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embeddings_gemini():
    embeddings_genai = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )
    return embeddings_genai
