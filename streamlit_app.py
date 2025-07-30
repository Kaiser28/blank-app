import streamlit as st
from qdrant_client import QdrantClient

st.title("🎈 Recherche de vecteurs Qdrant")

# Connexion à Qdrant (par défaut sur localhost)
client = QdrantClient(url="http://localhost:6333")

# Lancer la recherche lorsqu'on appuie sur le bouton
if st.button("Lancer la recherche"):
    query_vector = [0.1, 0.2, 0.3]
    hits = client.search(
        collection_name="ma_collection",
        query_vector=query_vector,
        limit=5,
    )
    st.write(hits)
