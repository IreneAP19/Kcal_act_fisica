import streamlit as st
import pickle
import numpy as np
import utils
import plotly.express as px
from PIL import Image
from sklearn.preprocessing import PolynomialFeatures
from streamlit_option_menu import option_menu  


st.set_page_config(page_title="Calculadora IMC y Kcal", layout="wide")

# Cargar modelos
@st.cache_data
def cargar_modelo_ob_cop():
    with open("../modelos/rnd_ob_cop.pkl", "rb") as model_rnd_ob_cop:
        return pickle.load(model_rnd_ob_cop)

@st.cache_data
def cargar_modelo():
    with open("../modelos/pol2_ejer.pkl", "rb") as model_pol2_ejer:
        return pickle.load(model_pol2_ejer)

@st.cache_data
def cargar_polynomial_features():
    with open("../modelos/pol2_transform_ejer.pkl", "rb") as pol_transf_ejer:
        return pickle.load(pol_transf_ejer)
def cargar_modelo_ob():
    with open("../modelos/pol2_ob.pkl", "rb") as model_pol2_ob:
        return pickle.load(model_pol2_ob)
@st.cache_data
def cargar_polynomial_features_ob():
    with open("../modelos/pol2_transform_ob.pkl", "rb") as pol_transf_ob:
        return pickle.load(pol_transf_ob)

modelo_ob_cop = cargar_modelo_ob_cop()
modelo_ob = cargar_modelo_ob()
modelo = cargar_modelo()
pol_2 = cargar_polynomial_features()
pol_2_ob = cargar_polynomial_features_ob()
import streamlit as st
from streamlit_option_menu import option_menu  

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #ff9a9e, #fad0c4, #ffdde1, #a18cd1, #fbc2eb);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #ff9a9e, #fad0c4);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Personalización de los estilos
styles = {
    # Estilo del contenedor principal con el degradado de fondo
    "main_container": {
        "background": "linear-gradient(to right, #6a0dad, #ff66cc)",  # Degradado de morados y rosas
        "color": "white",  # Color de texto blanco
        "padding": "20px",
    },
    # Estilo del menú de la barra lateral
    "menu": {
        "color": "white",
        "background-color": "#D8BFD8",  # Fondo sólido del menú
        "font-size": "16px",
    },
    # Estilo de la opción seleccionada en el menú
    "menu_selected": {
        "background-color": "#D8BFD8",  
        "color": "white",
    },
    # Estilo de los iconos del menú
    "icon": {
        "font-size": "20px",
        "color": "white",
    },
    # Estilo de las barras de selección (sliders, inputs, etc.)
    "input": {
        "background-color": "#D8BFD8", 
        "color": "white",
        "border-radius": "5px",
    },
    # Estilo para los botones de predicción (en tonos morados)
    "button": {
        "background-color": "#E6E6FA", 
        "color": "white",
        "padding": "10px 20px",
        "border-radius": "5px",
    }
}


# Menú con iconos en la barra lateral
with st.sidebar:
    opcion= option_menu(
        menu_title="Menú de Navegación 🦝",
        options=[
            "Inicio",
            "Cálculo de IMC",
            "Cálculo de Calorías de Ejercicio",
            "Estimación de kcal diarias y Recomendaciones",
            "Gráficos y Análisis"
        ],
        icons=[
            "house",
            "calculator",
            "activity",
            "fire",
            "bar-chart",
        ],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "10px", "background-color": styles["menu"]["background-color"]},
            "menu": styles["menu"],
            "menu_selected": styles["menu_selected"],
            "icon": styles["icon"],
        }
    )


if opcion == "Inicio":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image("../img/nombre.png")

    with col3:
        st.write(' ')
    st.title("Bienvenido a la Calculadora de IMC y Calorías Diarias")
    st.image("../img/lemur.png", width=250)
    st.write("Esta aplicación te ayudará a calcular tu Índice de Masa Corporal (IMC) y la cantidad de calorías diarias recomendadas según tu nivel de actividad. 💪 Por último, Maki te dará algunas recomendaciones según tu objetivo")


elif opcion == "Cálculo de IMC":
    st.title("⚖️ Cálculo de IMC")
    Age = st.number_input("Ingresa tu edad (años):", min_value=0, max_value=120, value=30)
    Male = st.selectbox("Selecciona tu género:", options=["Hombre", "Mujer"])
    Weight = st.number_input("Ingresa tu peso (kg):", min_value=30, max_value=200, value=70)
    Height = st.number_input("Ingresa tu altura (m):", min_value=1.0, max_value=2.5, value=1.75)
    #frecuencia_ejercicio = st.number_input("Frecuencia de ejercicio (días/semana):", min_value=0, max_value=7, value=3)
    family_with_overweight=st.selectbox("¿Antecedentes familiares de obesidad?:", options=["Si", "No"])
    opciones_alcohol = {
        "Nunca": 0,
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
    if st.button("Predecir", key="calcular_imc"):
    
        # Convertir la entrada en un array numérico
        entrada_ob = np.array([[Age,Height, Weight, family_with_overweight_valor,Alcohol,Andar_bici_valor,Control_kcal_valor,FastFood_valor,Male_valor]]).reshape(1, -1)
        
        entrada_kcal_ejer_pol2 = pol_2_ob.transform(entrada_ob)
        prediccion_ob = modelo_ob.predict(entrada_kcal_ejer_pol2)
        st.write(f"📊 **IMC Calculado:** {prediccion_ob[0]:.2f}")

        datos_usuario = {
            "BMI": prediccion_ob[0],  # Usamos la salida del primer modelo como BMI
            "Age": Age,  # Edad
            "Male": Male_valor  # Sexo (1=Hombre, 0=Mujer)
        }

        #  Aplicar la función de utils para calcular el % de grasa corporal
        porcentaje_grasa = utils.calcular_grasa_bmi(datos_usuario)
        st.write(f"**Porcentaje estimado de grasa corporal:** {porcentaje_grasa:.2f}%")

        
        prediccion_tipo = modelo_ob_cop.predict(entrada_ob)
        # prediccion_tipo = round(prediccion_tipo_ini[0])
        predic_tipo=utils.label(prediccion_tipo)
        st.write(f"**Clasificación:** {predic_tipo}")

        
        # Añadir barra de IMC interactiva con colores
        imc_value = prediccion_ob[0]
        colores = {
            'Infrapeso': 'red',
            'Normal': 'yellowgreen',
            'Sobrepeso': 'yellow',
            'Obesidad': 'red'
        }

        # Determinar la categoría y mostrar la barra con colores
        if imc_value < 18.5:
            arrow_position = "0%"
        elif 18.5 <= imc_value < 24.9:
            arrow_position = "40%"
        elif 24.9 <= imc_value < 27.9:
            arrow_position = "50%"
        elif 27.9 <= imc_value < 29.9:
            arrow_position = "60%"
        elif 29.9 <= imc_value < 34.9:
            arrow_position = "80%"
        elif 34.9 <= imc_value <= 39.9:
            arrow_position = "90%"
        else:
            arrow_position = "100%"
        # Mostrar barra de IMC con colores
        st.markdown(f"""
        <style>
        .imc-bar {{
            width: 100%;
            height: 20px;
            background: linear-gradient(to right, 
                red 0%, yellow 25%, yellowgreen 50%, yellow 75%, red 100%);
            border-radius: 10px;
            position: relative;
        }}
        .arrow {{
            position: absolute;
            top: -10px;
            left: {arrow_position};
            font-size: 30px;
            color: black;
        }}
        </style>
        <div class="imc-bar">
            <div class="arrow">↑</div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state["prediccion_ob"] =prediccion_ob[0]
        st.session_state["male"] = Male_valor
        st.session_state["weight"] = Weight
        st.session_state["height"] = Height
        st.session_state["age"] = Age
        st.session_state["porcentaje_grasa"] = porcentaje_grasa

elif opcion == "Cálculo de Calorías de Ejercicio":
    st.title("🔥 Cálculo de Calorías de Ejercicio")
    
    tipo_ejer = ['Yoga', 'Strength', 'Cardio', 'HIIT']

    Workout_Type = st.selectbox("¿Qué ejercicio va a realizar?", tipo_ejer)
    # Crear un vector con ceros
    Workout_Type_encoded = np.zeros(len(tipo_ejer))

    # Activar la posición correspondiente
    Workout_Type_encoded[tipo_ejer.index(Workout_Type)] = 1

    tiempo_str = st.text_input("Duración de la actividad física (Ej: 1h 30min):")
    Session_Duration = utils.convertir_tiempo_a_decimal(tiempo_str)

    # frecuencia = {
    #     '1-2 días': 2, 
    #     '3-4 días': 3, 
    #     '4-5 días': 4, 
    #     '6-7 días': 5
    # }
    # tipo_frec=[2,3,4,5]
    # W_Frequency = st.selectbox("¿Con qué frecuencia lo va a realizar?", frecuencia.keys())
    # Workout_Frequency = frecuencia[W_Frequency]  # Convertir a valor numérico
    # # Crear un vector con ceros
    # Workout_Frec_encoded = np.zeros(len(tipo_frec))

    # # Activar la posición correspondiente
    # Workout_Frec_encoded[tipo_frec.index(Workout_Frequency)] = 1

    # nivel = {
    #     'Nuevo/a': 1, 
    #     'Algo he hecho antes': 2, 
    #     'Soy un experto/a': 3
    # }
    # tipo_nivel=[1,2,3]
    # W_level = st.selectbox("¿Ha practicado antes este ejercicio?", nivel.keys())
    # Experience_Level = nivel[W_level]  # Convertir a valor numérico
    # Experience_Level_encoded = np.zeros(len(tipo_nivel))

    # # Activar la posición correspondiente
    # Experience_Level_encoded[tipo_nivel.index(Experience_Level)] = 1

    frecuencia = {
        '1-2 días': 2, 
        '3-4 días': 3, 
        '4-5 días': 4, 
        '6-7 días': 5
    }
    W_Frequency = st.selectbox("¿Con qué frecuencia lo va a realizar?", frecuencia.keys())
    Workout_Frequency = frecuencia[W_Frequency]  # Convertir a valor numérico

    # Botón para predecir calorías de ejercicio
    if st.button("Predecir kcal ejer", key="predecir kcal ejer"):
        if Session_Duration == 0:
            st.warning("Por favor, ingresa una duración válida para la actividad física.")
            
        else:
            # Crear nueva entrada para el segundo modelo
                                    
            entrada_kcal_ejer = np.array([[st.session_state["age"], st.session_state["weight"], st.session_state["height"], Session_Duration, st.session_state["porcentaje_grasa"], *Workout_Type_encoded,st.session_state["male"], st.session_state["prediccion_ob"]]]).reshape(1, -1)
            entrada_kcal_pol2 = pol_2.transform(entrada_kcal_ejer)

            try:
                # Predicción
                prediccion_final = modelo.predict(entrada_kcal_pol2)

                # Guardar datos en sesión
                st.session_state["kcal_ejer"] = prediccion_final[0]
                st.session_state["freq_ejer"] = Workout_Frequency        

                # Mostrar el resultado
                st.write(f"🔥 **Predicción calorías gastadas en actividad física:** {round(prediccion_final[0])}")
                if Workout_Type == "Yoga":
                    st.image("../img/yoga.png", width=250)
                elif Workout_Type in ["HIIT", "Cardio"]:
                    st.image("../img/hitt.png", width=250)
                else:
                    st.image("../img/fuerza.png", width=250)

                st.success("Datos guardados en la sesión correctamente.")

            except Exception as e:
                st.error(f"Error en la predicción: {e}")

elif opcion == "Estimación de kcal diarias y Recomendaciones":
    
    col1, col2 = st.columns(2)

    with col1:
        st.title("🥭 Kcal recomendadas y Macronutrientes")

    with col2:
        st.image("../img/comida.png", width=200)

   
    required_keys = ["male", "weight", "height", "age", "kcal_ejer", "prediccion_ob"]
    missing_keys = [key for key in required_keys if key not in st.session_state]

    if missing_keys:
        st.image("../img/warming.png", width=250)
        st.warning(f"Faltan datos por rellenar. Por favor, complete los campos anteriores.")
    else:
        try:
            objetivos=utils.objetivo(st.session_state["prediccion_ob"])
            st.session_state["objetivos"] = objetivos
            kcal_recomendadas = utils.gasto_calorico(
                st.session_state["male"],
                st.session_state["weight"],
                st.session_state["height"] * 100,  
                st.session_state["freq_ejer"],
                st.session_state["age"],
                st.session_state["kcal_ejer"]
            )
                
            st.write(f"**Calorías diarias recomendadas:** {kcal_recomendadas:.2f} kcal")
            st.session_state["kcal_rec"] = kcal_recomendadas
            # Calcular la distribución de macronutrientes
            for i, objetivo in enumerate(objetivos):
                # Calcular macronutrientes para el objetivo actual
                resultado_str, macronutrientes_dict = utils.calcular_macronutrientes(round(kcal_recomendadas, 2), st.session_state["male"], objetivo)

                # Guardar los macronutrientes en session_state
                st.session_state[f"macros_{objetivo}"] = macronutrientes_dict

                # Mostrar los valores
                st.write(f"**Distribución de Macronutrientes - Objetivo: {objetivo.capitalize()}**")
                st.write(f"Carbohidratos: {macronutrientes_dict['Carbohidratos (g)']}g")
                st.write(f"Proteinas: {macronutrientes_dict['Proteinas (g)']}g")
                st.write(f"Grasas: {macronutrientes_dict['Grasas (g)']}g")
        except KeyError as e:
                st.warning(f"No se pudieron calcular los macronutrientes para el objetivo '{objetivo}'. Error: {e}")
                
        recomendaciones = utils.recomendaciones(st.session_state["prediccion_ob"])
        st.write(recomendaciones)
    
if opcion == "Gráficos y Análisis":
    st.title("📈 Análisis Visual")
    required_keys = ["male", "weight", "height", "age", "kcal_ejer", "prediccion_ob"]
    missing_keys = [key for key in required_keys if key not in st.session_state]

    if missing_keys:
        st.image("../img/warming.png", width=250)
        st.warning(f"Faltan datos por rellenar. Por favor, complete los campos anteriores.")
    else:
        try:
            datos = {
                "Categoría": ["Kcal totales", "Kcal ejercicio", "Kcal sin ejercicio"],
                "Kcal": [st.session_state["kcal_rec"], st.session_state["kcal_ejer"], st.session_state["kcal_rec"] - st.session_state["kcal_ejer"]]
            }
            fig = px.bar(datos, x="Categoría", y="Kcal", color="Categoría",
                        color_discrete_sequence=["#ff9a9e", "#fad0c4", "#a18cd1"],
                        title="Distribución del Gasto Calórico")
            st.plotly_chart(fig)
        #-------------------------
            objetivos=st.session_state["objetivos"]

            for i, objetivo in enumerate(objetivos):
                try:
                    # Obtener los macronutrientes guardados en session_state
                    macros = st.session_state.get(f"macros_{objetivo}", {})

                    # Crear el diccionario de datos para la gráfica
                    datos1 = {
                        "Macronutrientes": ["CH", "Proteinas", "Grasas"],
                        "Gramos": [
                            macros.get("Carbohidratos (g)", 0),
                            macros.get("Proteinas (g)", 0),
                            macros.get("Grasas (g)", 0)
                        ]
                    }

                    # Crear la gráfica
                    fig1 = px.pie(
                        datos1,
                        names="Macronutrientes",
                        values="Gramos",
                        color="Macronutrientes",
                        title=f"Distribución de Macronutrientes - Objetivo: {objetivo.capitalize()}",
                        color_discrete_sequence=["#ff9a9e", "#fad0c4", "#a18cd1"]
                    )

                    # Mostrar la gráfica en la columna correspondiente
                    st.plotly_chart(fig1, use_container_width=True)
                    

                except KeyError:
                    st.warning(f"No se pudieron obtener los datos para el objetivo: {objetivo}.")
        # datos1 = {
        #     "Macronutrientes": ["CH", "Proteinas", "Grasas"],
        #     "Gramos": [st.session_state["Ch"], st.session_state["Prot"], st.session_state["Gras"]]
        # }
        # fig1 = px.bar(datos1, x="Macronutrientes", y="Gramos", color="Macronutrientes",
        #             color_discrete_sequence=["#ff9a9e", "#fad0c4", "#a18cd1"],
        #             title="Distribución de Macronutrientes")
        # st.plotly_chart(fig1)
            st.image("../img/final.png", width=250)
        except KeyError:
            st.warning("Si los campos anteriores están vacíos, no se pueden visualizar las gráficas.")

