from ragas.testset import TestsetGenerator
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader

import getpass
import os

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

path = "rag/src/"
loader = DirectoryLoader(path, glob="**/*.pdf")
docs = loader.load()

generator_llm = LangchainLLMWrapper(
        ChatOpenAI(
            model='gpt-4o-mini'
        )
)
generator_embedding = LangchainEmbeddingsWrapper(
    OpenAIEmbeddings(
        model='text-embedding-ada-002'
    )
)

generator = TestsetGenerator(
    llm=generator_llm,
    embedding_model=generator_embedding,
)
dataset = generator.generate_with_langchain_docs(
    documents=docs,
    testset_size=5,
    with_debugging_logs=True
)

result = dataset.to_pandas()
result.to_csv("testset.csv", index=False)

print(dataset.to_pandas())


