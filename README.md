
![Texto alternativo](img/lemur.png)
# 📊 Aplicación de Cálculo de IMC y Calorías Quemadas

Este proyecto de **Machine Learning** tiene como finalidad crear una aplicación desarrollada con Streamlit que permite calcular el índice de masa corporal (IMC), el porcentaje de grasa corporal y estimar las calorías quemadas durante el ejercicio. Además, recomienda la ingesta calórica diaria según los objetivos del usuario.

---

## 🚀 Características
- **Cálculo del IMC** y clasificación en distintas categorías (infrapeso, normal, sobrepeso, obesidad).
- **Estimación del porcentaje de grasa corporal** basado en el IMC y otros factores.
- **Cálculo de calorías quemadas** según el tipo de ejercicio y características del usuario.
- **Recomendaciones personalizadas** de ingesta calórica según objetivos (mantener, subir o bajar de peso).
- **Posible integración futura** con un modelo no supervisado para sugerir menús ajustados a las calorías recomendadas.

---

📂 repositorio

  │-- 📁 img/                # Imágenes usadas en la app 
  
  │-- 📁 models/             # Modelos de Machine Learning 

  │-- 📁 data/               # Datos utilizados en la app y de prueba 
  
      |--raw                 # Datos sin procesar 
      
      |-- train/test         # Datos procesados 
      
  │-- 📁 src/ 
  
      │-- 📄 train.py        # Entreno de los modelos finales
      
      │-- 📄 limieza.py      # EDA 
      
      │-- 📄 utils.py        #Funciones necesarias
      
  │-- 📁 notebooks/
  
      │-- 📄 clasificacion.ipynb
      
      │-- 📄 calcular kcla ejer.ipynb 
      
      │-- 📄 calcular IMC.ipynb 
      
  │-- 📁 docs/ 
  
      │-- 📄 memoria
      
      │-- 📄 presentaciones
      
  │-- 📁 streamlit/ 
  
      │-- 📄 app.py          # Archivo principal de la aplicación 
      
      │-- 📄 utils.py        # Funciones auxiliares
      
│-- 📄 README.md # Este archivo

## Modelos Utilizados

- **Modelos de Regresión Lineal para IMC y Calorías Quemadas**: Este modelo predice el IMC, el porcentaje de grasa corporal y las calorías quemadas en función de los datos proporcionados por el usuario.
- **Modelos de Clasificación**: Predice la categoria a la que el usuario pertenece en función a su IMC.
  
## Tecnologías y Herramientas

- **Python**: Lenguaje principal del proyecto.
- **Streamlit**: Framework utilizado para la interfaz de usuario.
- **Scikit-learn**: Para la implementación de los modelos de Machine Learning.
- **Pandas**: Para la manipulación de datos.
- **Numpy**: Para cálculos numéricos.

