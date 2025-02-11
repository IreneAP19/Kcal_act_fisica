import streamlit as st
import pickle
import numpy as np
import utils 

# Cargar los modelos
@st.cache_data
def cargar_modelo_ob():
    with open("../modelos/rnd_reg_obesity.pkl", "rb") as f:
        modelo = pickle.load(f)
    return modelo

@st.cache_data
def cargar_modelo():
    with open("../modelos/rrnd_reg.pkl", "rb") as f:
        modelo = pickle.load(f)
    return modelo

modelo_ob = cargar_modelo_ob()
modelo = cargar_modelo()

#Título de la App
st.title("Predicción con Dos Modelos en Streamlit 🚀")

#  Entrada del usuario
valores_input = st.text_input("Ingresa los valores separados por comas para el primer modelo", "")

# Botón para predecir
if st.button("Predecir"):
    try:
        # Convertir la entrada en un array numérico
        entrada_ob = np.array([list(map(float, valores_input.split(",")))]).reshape(1, -1)

        # Predicción con el primer modelo (Obesidad)
        prediccion_ob = modelo_ob.predict(entrada_ob)
        st.write(f"📊 **Predicción del primer modelo (Obesidad):** {prediccion_ob[0]}")

        datos_usuario = {
            "BMI": prediccion_ob[0],  # Usamos la salida del primer modelo como BMI
            "Age": entrada_ob[0, 1],  # Edad
            "Male": int(entrada_ob[0, 2])  # Sexo (1=Hombre, 0=Mujer)
        }

        # 🔹 Aplicar la función de utils para calcular el % de grasa corporal
        porcentaje_grasa = utils.calcular_grasa_bmi(datos_usuario)
        st.write(f"**Porcentaje estimado de grasa corporal:** {porcentaje_grasa:.2f}%")

        imc_clasificacion=utils.clasificar_bmi(porcentaje_grasa)
        st.write(f"**Clasificación según el porcentaje graso:** {imc_clasificacion}")




        # 🔹 Crear nueva entrada para el segundo modelo
        nueva_entrada = np.hstack([entrada_ob, np.array([[porcentaje_grasa]])])

        # Usar la salida del primer modelo como entrada para el segundo
        nueva_entrada = np.hstack([entrada_ob, prediccion_ob.reshape(-1, 1)])

        # Verificar que la nueva entrada tiene el tamaño correcto
        if nueva_entrada.shape[1] != modelo.n_features_in_:
            st.error(f"⚠️ Error: El segundo modelo espera {modelo.n_features_in_} valores, pero recibió {nueva_entrada.shape[1]}.")
        else:
            #  Predicción con el segundo modelo
            prediccion_final = modelo.predict(nueva_entrada)
            st.success(f"📊 **Predicción calorias gastadas en actividad fisica:** {prediccion_final[0]}")

            datos_usuario1 = {
                "Male": int(entrada_ob[0, 3]),
                "Peso": int(entrada_ob[0, 4]), 
                "freq_ejer": int(),
                "Age": entrada_ob[0, 1],  # Edad
                "Male": int(entrada_ob[0, 2]),  # Sexo (1=Hombre, 0=Mujer)
                "kcla_ejer":prediccion_final[0]

        }

        # 🔹 Aplicar la función de utils para calcular el % de grasa corporal
        porcentaje_grasa = utils.calcular_grasa_bmi(datos_usuario)
        st.write(f"**Porcentaje estimado de grasa corporal:** {porcentaje_grasa:.2f}%")


    except ValueError:
        st.error("⚠️ Asegúrate de ingresar valores numéricos separados por comas.")






