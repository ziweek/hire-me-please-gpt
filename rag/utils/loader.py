from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

def load_pdf(file_path: str):
    loader = PyPDFLoader(
        file_path=file_path
    )
    loaded_document = loader.load()
    print(f"utils/loader.py loaded {len(loaded_document)} documents")
    return loaded_document
