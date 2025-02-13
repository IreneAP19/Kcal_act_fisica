import streamlit as st
import pickle
import numpy as np
import utils 


st.set_page_config(page_title="Calculadora IMC y Kcal", layout="centered")
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

# Estilos personalizados con CSS
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #ff9a9e, #fad0c4, #ffdde1, #a18cd1, #fbc2eb);
        }
        .title {
            font-size: 30px;
            font-weight: bold;
            color:rgb(20, 119, 117);
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()


# Pantalla principal explicativa
st.markdown("# Bienvenido a la Calculadora de IMC y Calorías Diarias 🏋️‍♂️")
st.write("Esta aplicación te ayudará a calcular tu Índice de Masa Corporal (IMC) y la cantidad de calorías diarias recomendadas según tu nivel de actividad. 💪")
st.write("### ¿Cómo funciona?")
st.write("1️⃣ Ingresa tus datos como peso, altura y edad.")
st.write("2️⃣ Presiona el botón calcular y obtendrás tu IMC.")
st.write("3️⃣ Selecciona tu nivel de actividad física, ejercico que quieres realizar....")
st.write("4️⃣ Presiona el botón calcular y obtendrás la kcal que gastarás y la recomendación de ingesta calórica diaria.")
st.write("---")

# Carga de imagen
# top_image = Image.open("fitness.png")
# st.image(top_image, use_column_width=True)

# Entrada del usuario con texto explicativo
Age = st.number_input("Ingresa tu edad (años):", min_value=0, max_value=120, value=30)
Male = st.selectbox("Selecciona tu género:", options=["Hombre", "Mujer"])
Weight = st.number_input("Ingresa tu peso (kg):", min_value=30, max_value=200, value=70)
Height = st.number_input("Ingresa tu altura (m):", min_value=1.0, max_value=2.5, value=1.75)
#frecuencia_ejercicio = st.number_input("Frecuencia de ejercicio (días/semana):", min_value=0, max_value=7, value=3)
family_with_overweight=st.selectbox("¿Antecedentes familiares de obesidad?:", options=["Si", "No"])
opciones_alcohol = {
    "No": 0,
    "A veces": 1,
    "Mucha fecuencia": 2,
    "Todos los dias": 3
}
consumo_alcohol = st.selectbox("¿Con qué frecuencia consumes alcohol?", opciones_alcohol.keys())
Alcohol = opciones_alcohol[consumo_alcohol]  # Convertir a valor numérico
Andar_bici=st.selectbox("¿Va al lugar de trabajo/estudio andando o en bici?:", options=["Si", "No"])
Control_kcal=st.selectbox("¿Controla las kcal que toma al día?:", options=["Si", "No"])
FastFood=st.selectbox("¿Suele consumir 'FastFood'?:", options=["Si", "No"])

#Convertir a numerico
family_with_overweight_valor = 1 if family_with_overweight == "Si" else 0
Andar_bici_valor = 1 if Andar_bici == "Si" else 0
Male_valor = 1 if Male == "Hombre" else 0
Control_kcal_valor = 1 if Control_kcal == "Si" else 0
FastFood_valor = 1 if FastFood == "Si" else 0

# Botón para predecir
if st.button("Predecir"):
    try:
        # Convertir la entrada en un array numérico
        entrada_ob = np.array([[Age,Height, Weight, family_with_overweight_valor,Alcohol,Andar_bici_valor,Control_kcal_valor,FastFood_valor,Male_valor]]).reshape(1, -1)

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

        imc_clasificacion=utils.clasificar_bmi(prediccion_ob[0])
        st.write(f"**Clasificación según el porcentaje graso:** {imc_clasificacion}")


        # # Añadir barra de IMC interactiva con colores
        # imc_value = prediccion_ob[0]
        # colores = {
        #     'Infrapeso': 'red',
        #     'Normal': 'yellowgreen',
        #     'Sobrepeso': 'yellow',
        #     'Obesidad': 'red'
        # }

        # # Determinar la categoría y mostrar la barra con colores
        # if imc_value < 18.5:
        #     arrow_position = "0%"  # Infrapeso
        # elif 18.5 <= imc_value < 24.9:
        #     arrow_position = "25%"  # Normal
        # elif 25 <= imc_value < 29.9:
        #     arrow_position = "50%"  # Sobrepeso
        # else:
        #     arrow_position = "75%"  # Obesidad
        # # Mostrar barra de IMC con colores
        # st.markdown(f"""
        # <style>
        # .imc-bar {{
        #     width: 100%;
        #     height: 20px;
        #     background: linear-gradient(to right, 
        #         red 0%, yellow 25%, yellowgreen 50%, yellow 75%, red 100%);
        #     border-radius: 10px;
        #     position: relative;
        # }}
        # .arrow {{
        #     position: absolute;
        #     top: -10px;
        #     left: {arrow_position};
        #     font-size: 30px;
        #     color: black;
        # }}
        # </style>
        # <div class="imc-bar">
        #     <div class="arrow">↑</div>
        # </div>
        # """, unsafe_allow_html=True)
#--------------Nueva entrada para el segundo modelo
        tipo_ejer = {
           'Yoga': 0, 
           'Strength': 1, 
           'Cardio': 2, 
           'HIIT': 3
        }
        Workout_Type = st.selectbox("¿Qué ejercicio va a realizar?", tipo_ejer.keys())
        Workout_Type_value = tipo_ejer[Workout_Type]  # Convertir a valor numérico
        tiempo_str = st.text_input("Duración de la actividad física (Ej: 1h 30min):", )

        Session_Duration = utils.convertir_tiempo_a_decimal(tiempo_str)

        frecuencia = {
           '1-2 días': 2, 
           '3-4 días': 3, 
           '4-5 días': 4, 
           '6-7 días': 5
        }
        W_Frequency = st.selectbox("¿Con qué frecuencia lo va a realizar?", frecuencia.keys())
        Workout_Frequency = frecuencia[W_Frequency]  # Convertir a valor numérico
        
        nivel = {
           'Nuevo/a': 1, 
           'Algo he hecho antes': 2, 
           'Soy un experto/a': 3
        }
        W_level = st.selectbox("¿A practicado antes este ejercicio?", nivel.keys())
        Experience_Level = nivel[W_level]  # Convertir a valor numérico

        # 🔹 Crear nueva entrada para el segundo modelo
        entrada_kcal_ejer = np.array([[Age, Weight,Height,Session_Duration,np.array([[porcentaje_grasa]]),Workout_Frequency,Experience_Level,Workout_Type_value,Male_valor,np.array([[prediccion_ob[0]]])]]).reshape(1, -1)

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






