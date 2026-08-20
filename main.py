import streamlit as st
import seaborn as sns

st.title("Aplicación Ejemplo Despliegue")

st.write("Hola mundo")

st.dataframe(sns.load_dataset("iris"))

st.write(st.secrets)