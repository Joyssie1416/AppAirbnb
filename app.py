import streamlit as st
from pymongo import MongoClient

MONGO_URI = st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)
db = client["sample_airbnb"]
collection = db["listingsAndReviews"]

st.title("Buscar propiedades Airbnb por ciudad")

ciudad = st.text_input("Ingresa una ciudad:")

if st.button("Buscar"):
    resultados = collection.find({"address.market": ciudad})
    lista = []
    for r in resultados:
        lista.append(r)
    st.write(f"Total encontrados: {len(lista)}")
    for item in lista:
        st.write(item.get("name", "Sin nombre"))