import streamlit as st

st.title("Mi primera app con Streamlit 🚀")

# Entrada de texto
nombre = st.text_input("¿Cómo te llamas?", "")

# Botón
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}! 👋")


