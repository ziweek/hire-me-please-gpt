from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, OnlinePDFLoader

def load_local_pdf(file_path: str):
    loader = PyPDFLoader(
        file_path=file_path
    )
    loaded_document = loader.load()
    print(f"utils/loader.py loaded {len(loaded_document)} documents")
    return loaded_document

def load_online_pdf(file_path: str):
    loader = OnlinePDFLoader(
        file_path="https://drive.google.com/file/d/1HHSJZPatsZDjIVnxAeOsU2fK-CFdYiAK/view?usp=sharing"
    )
    loaded_document = loader.load()
    print(f"utils/loader.py loaded {len(loaded_document)} documents")
    return loaded_document
