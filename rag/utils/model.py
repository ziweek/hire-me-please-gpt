from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAI

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from langchain import hub

from langchain_community.vectorstores import FAISS
from .embed import get_embeddings_gemini
import streamlit as st

import pprint

def run_llm(query: str):
    llm = GoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        api_key=st.secrets["GOOGLE_API_KEY"]
        )
    
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=retrieval_qa_chat_prompt
    )
    
    vector_store = FAISS.load_local(
        folder_path="rag/faiss_index_HireMePleaseGPT",
        embeddings=get_embeddings_gemini(),
        allow_dangerous_deserialization=True
    )
    retrieval_chain = create_retrieval_chain(
        retriever=vector_store.as_retriever(),
        combine_docs_chain=combine_docs_chain,
    )
    
    result = retrieval_chain.invoke(
        input={
            "input": query
            }
        )
    result = StrOutputParser().parse(text=result)
    return result


if __name__ == "__main__":
    print("utils/model.py is running...")
    context_result = run_llm("tell me about Project experience")
    pprint.pprint(context_result)
