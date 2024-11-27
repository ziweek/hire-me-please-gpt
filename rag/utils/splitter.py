import os
from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(raw_documents):
    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    splitted_documents = text_spliter.split_documents(documents=raw_documents)
    print(f"utils/splitter.py splitted {len(splitted_documents)} documents")
    return splitted_documents