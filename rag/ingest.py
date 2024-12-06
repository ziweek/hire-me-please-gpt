from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS

from utils.loader import load_local_pdf, load_online_pdf
from utils.splitter import split_documents
from utils.embed import get_embeddings_gemini
from utils.utils import load_yaml_file



def ingest_documents(file_path):
    raw_documents = load_local_pdf(file_path=file_path)
    splitted_documents = split_documents(raw_documents=raw_documents)
    embeddings_huggingface = get_embeddings_gemini()
    
    print("ingest.py ingesting...")
    vector_store = FAISS.from_documents(
        documents=splitted_documents,
        embedding=embeddings_huggingface
        )
    vector_store.save_local("faiss_index_HireMePleaseGPT")
    print("ingest.py ingested")
    
def ingest_multiple_documents(dict_documents: dict):
    loaded_documents = []
    for document, file_path in dict_documents.items():
        loaded_document = load_local_pdf(file_path=file_path)
        loaded_documents.extend(loaded_document)
        print(f"Splitted {document}")
    splitted_documents = split_documents(raw_documents=loaded_documents)
    embeddings_gemini = get_embeddings_gemini()
    
    print("ingest.py ingesting...")
    vector_store = FAISS.from_documents(
        documents=splitted_documents,
        embedding=embeddings_gemini
        )
    vector_store.save_local("faiss_index_HireMePleaseGPT")
    print("ingest.py ingested")

if __name__ == "__main__":
    # ingest_documents("rag/src/8A-Blue-Book-en.pdf")
    documents = {
        "resume-llm-engineer": load_yaml_file("config.yaml")['resume_file_path'],
    }
    ingest_multiple_documents(documents)