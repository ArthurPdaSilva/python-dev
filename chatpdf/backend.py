from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

folder_files = Path(__file__).parent / "files"
model_name = "gpt-3.5-turbo-0125"

def import_docs():
    docs = []
    for file in folder_files.glob("*.pdf"):
        loader = PyPDFLoader(file)
        docs.extend(loader.load())
    return docs

def split_docs(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50, separators=["\n\n", "\n", " ", "", "."])
    docs = text_splitter.split_documents(docs)
    for i, doc in enumerate(docs):
        doc.metadata["source"] = doc.metadata["source"].split("/")[-1]
        doc.metadata["doc_id"] = i

    return docs

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store

def create_chain_conversa():
    docs = import_docs()

    if not docs:
        st.error("Nenhum documento encontrado. Faça o upload de um arquivo PDF.")
        return

    docs = split_docs(docs)
    vector_store = create_vector_store(docs)

    llm = ChatOpenAI(model=model_name)
    chain = ConversationBufferMemory(return_messages=True, memory_key="chat_history", output_key="answer")
    retriever = vector_store.as_retriever()
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=chain,
        retriever=retriever,
        return_source_documents=True,
        verbose=True
    )

    st.session_state["chain"] = chat_chain
    return chat_chain