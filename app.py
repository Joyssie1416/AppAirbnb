import streamlit as st
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Joystick2:Olaf11022002XD5@clusterjoystick2.hajswhe.mongodb.net/?appName=ClusterJoystick2"

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