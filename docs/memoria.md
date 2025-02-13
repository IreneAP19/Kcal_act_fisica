
#**Aplicación de Cálculo de IMC, Calorías Quemadas y Recomendación de Ingesta Calórica Diaria**

## Resumen del Proyecto

El objetivo de este proyecto es desarrollar una aplicación que, con unos pocos datos básicos sobre el usuario, sea capaz de calcular su Índice de Masa Corporal (IMC), estimar el porcentaje de grasa corporal, la categoría en la que se encuentra (como infrapeso, sobrepeso, etc.) y calcular las calorías que se quemarán durante la actividad física. Además, a partir de las calorías quemadas y de los objetivos del usuario, la aplicación recomienda una ingesta calórica diaria adecuada para mantener, perder o ganar peso.

El proyecto está basado en un modelo de Machine Learning, específicamente una regresión lineal, que toma como entradas variables como el peso, la altura, la edad, el sexo, entre otros. Esta información es utilizada para hacer predicciones personalizadas, mejorando la salud y el bienestar de los usuarios.

## Descripción del Proyecto

La aplicación consiste en una serie de pasos interactivos que el usuario debe seguir para recibir recomendaciones personalizadas. El flujo es el siguiente:

1. **Cálculo del IMC**: El usuario ingresa su edad, peso, altura, sexo..., y la aplicación calcula su IMC.
2. **Porcentaje de Grasa Corporal y Clasificación**: A partir del IMC calculado, la aplicación estima el porcentaje de grasa corporal y clasifica al usuario en diferentes categorías (infrapeso, peso normal, sobrepeso, obesidad).
3. **Estimación de Calorías Quemadas**: El usuario ingresa información adicional sobre la actividad física que va a realizar (tipo de ejercicio, frecuencia y duración). Con esta información y las características del usuario, el modelo estima las calorías que se quemarán durante la actividad física.
4. **Recomendación de Ingesta Calórica Diaria**: A partir de las calorías quemadas, la aplicación recomienda una ingesta calórica diaria basada en los objetivos del usuario (mantener, subir o bajar de peso).

## Metodología

Para cada paso del proceso, se utilizaron modelos de Machine Learning para hacer predicciones precisas. En particular, para los cálculos relacionados con el IMC y las calorías quemadas, se utilizó un modelo de regresión lineal, entrenado con un conjunto de datos sintéticos representativo de la población general.

### 1. **Modelo de Regresión para el IMC**
El primer paso consiste en el cálculo del IMC. Para ello, se utiliza un modelo de regresión lineal que, a partir de los datos ingresados por el usuario (peso, altura, edad, etc.), calcula el IMC de manera precisa. 

### 2. **Modelo para Estimar el Porcentaje de Grasa Corporal**
A partir del IMC calculado, el modelo utiliza fórmulas y funciones definidas para estimar el porcentaje de grasa corporal. Esto se hace con base en una regresión lineal que toma el IMC y otros factores relacionados para hacer la predicción.

### 3. **Modelo para Calorías Quemadas**
El siguiente paso es calcular las calorías quemadas durante la actividad física. Aquí, se utiliza un modelo de regresión que tiene en cuenta variables como el tipo de ejercicio, la frecuencia, la duración de la actividad, y las características personales del usuario (sexo, peso, edad, etc.).

### 4. **Recomendación de Ingesta Calórica Diaria**
Una vez que las calorías quemadas han sido estimadas, el siguiente paso es recomendar las calorías que el usuario debe consumir diariamente. Dependiendo de si el usuario desea mantener su peso, subir o bajar de peso, el modelo ajusta esta recomendación en función de las calorías quemadas y sus objetivos.

## Datos y Preprocesamiento

Los datos utilizados para entrenar los modelos provienen de una combinación de datos sintéticos generados para representar diferentes tipos de alimentos, su contenido calórico, y las categorías relacionadas (carbohidratos, proteínas, grasas). Además, se incluyeron características del usuario como su sexo, edad, peso y altura.

### Preprocesamiento de Datos:
- **Normalización**: Todos los datos numéricos (como peso, altura, etc.) fueron normalizados para mejorar el rendimiento del modelo de regresión.
- **Categorías**: Las variables categóricas como el sexo y el tipo de ejercicio se transformaron en variables numéricas para que pudieran ser procesadas por el modelo.
- **Validación de Datos**: Se aseguraron que los datos ingresados por los usuarios fueran válidos para evitar errores en el proceso de predicción.

## Resultados y Evaluación

El modelo fue entrenado utilizando un conjunto de datos de entrenamiento y evaluado con un conjunto de datos de prueba. Los resultados mostraron que el modelo de regresión lineal proporcionó predicciones precisas para el IMC y las calorías quemadas, lo que permite ofrecer recomendaciones personalizadas a los usuarios.

### Métricas de Evaluación:
- **Error Absoluto Medio (MAE)**: Para medir cuán cercanas son las predicciones del modelo en comparación con los valores reales.
- **Error Cuadrático Medio (MSE)**: Utilizado para evaluar la precisión del modelo, con un enfoque en las predicciones más erróneas.
- **Pérdida**: Se observó la reducción en la función de pérdida durante el entrenamiento, indicando la mejora del modelo a medida que se ajustaba.

## Herramientas y Tecnologías

- **Python**: Lenguaje de programación utilizado para el desarrollo de los modelos.
- **Streamlit**: Framework utilizado para construir la aplicación web interactiva que permite a los usuarios ingresar sus datos y obtener predicciones.
- **Scikit-learn**: Librería utilizada para implementar los modelos de regresión lineal.
- **Pandas y Numpy**: Utilizadas para el manejo y manipulación de los datos.
- **Pickle**: Utilizado para guardar y cargar los modelos entrenados.

## Conclusiones

El proyecto ha permitido desarrollar una aplicación capaz de calcular el IMC, estimar el porcentaje de grasa corporal, y predecir las calorías quemadas durante una actividad física, todo basado en modelos de regresión lineales. Con una interfaz fácil de usar, el usuario puede obtener recomendaciones personalizadas para mejorar su salud y bienestar.

Aunque el modelo de recomendación de menús aún no está listo, los modelos de IMC y calorías quemadas funcionan de manera eficiente y proporcionan una base sólida para continuar con el desarrollo de la aplicación.

## Futuro del Proyecto

El siguiente paso será completar el modelo de recomendación de menús basado en las calorías diarias recomendadas, utilizando un enfoque no supervisado. Además, se podría explorar la integración de más datos para mejorar la precisión de las predicciones y la experiencia del usuario.
