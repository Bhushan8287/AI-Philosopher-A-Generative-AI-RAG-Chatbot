import os
import streamlit as st
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

# Loading embeddings 
embedding = OllamaEmbeddings(model="nomic-embed-text")

# Loading the persisted Chroma DB
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding
)

# Creating retriever
retriever = vectordb.as_retriever()

# Setting up the prompt
prompt = ChatPromptTemplate.from_template(
    """You are an AI Philosopher. Use the following context to answer the user's question.
    If you don't know the answer, say you don't know.

    Context: {context}

    Question: {question}
    """
)

# Setring up the LLM
llm = Ollama(model="gemma3:1b")

# Creating the RetrievalQA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

# Streamlit interface
st.title("AI Philosopher")
st.write("Ask me things related to philosophy!")

query = st.text_input("Your Question:")

if query:
    result = qa_chain.invoke({"query": query})
    st.write(f"Answer: {result['result']}")