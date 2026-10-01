import chromadb
import streamlit as st
from ollama import chat
from sentence_transformers import SentenceTransformer

st.set_page_config(page_tittle="technova cocierge", layout="wide")

@st.cache_resource
def load_resources():
    model=SentenceTransformer('all_MiniM-L6-V2')
    client = chromadb.persistentclient(path="croma_db")
    return model, collection
model, collection = load_resources()
st.tittle("Nova, the Technova conceirge")
st.caption("I only know the fest documents. ask me anything about Technova")
