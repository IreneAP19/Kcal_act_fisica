from sklearn.metrics import mean_squared_error,mean_absolute_error
import seaborn as sns
def clasificar_bmi(imc):
    if imc < 18.5:
        return 'Insufficient_Weight'
    elif 18.5 <= imc < 24.9:
        return 'Normal_Weight'
    elif 24.9 <= imc < 27.9:
        return 'Overweight_Level_I'
    elif 27.9 <= imc < 29.9:
        return 'Overweight_Level_II'
    elif 29.9 <= imc < 34.9:
        return 'Obesity_Type_I'
    elif 34.9 <= imc <= 39.9:
        return 'Obesity_Type_II'
    else:
        return 'Obesity_Type_III'
    
#--------------------------------------------------------------

def calcular_grasa_bmi(row):

    bmi = row["BMI"]
    edad = row["Age"]
    sexo = row["Male"]  # 1 para hombres, 0 para mujeres

    if sexo == 1:
        return 1.20 * bmi + 0.23 * edad - 16.2
    else:
        return 1.20 * bmi + 0.23 * edad - 5.4  

#--------------------------------------------------------------   

# def calcular_macronutrientes(calorias_totales):
#     carb_cal = 0.50 * calorias_totales
#     prot_cal = 0.35 * calorias_totales
#     gras_cal = 0.15 * calorias_totales

#     carb_g = carb_cal / 4
#     prot_g = prot_cal / 4
#     gras_g = gras_cal / 9

#     resultado_str = f"Gramos de carbohidratos: {round(carb_g)}\nGramos de proteinas: {round(prot_g)}\nGramos de grasa: {round(gras_g)}"

#     macronutrientes_dict = {
#         "Carbohidratos (g)": round(carb_g),
#         "Proteinas (g)": round(prot_g),
#         "Grasas (g)": round(gras_g)
#     }

#     return resultado_str, macronutrientes_dict
def calcular_macronutrientes(calorias_totales, sexo, objetivo):
    # Ajustes según el sexo y el objetivo
    if sexo == 1:
        if objetivo == "mantener":
            carb_ratio, prot_ratio, gras_ratio = 0.50, 0.35, 0.15
        elif objetivo == "ganar":
            carb_ratio, prot_ratio, gras_ratio = 0.55, 0.30, 0.15
        elif objetivo == "perder":
            carb_ratio, prot_ratio, gras_ratio = 0.40, 0.40, 0.20
    elif sexo == 0:
        if objetivo == "mantener":
            carb_ratio, prot_ratio, gras_ratio = 0.50, 0.25, 0.25
        elif objetivo == "ganar":
            carb_ratio, prot_ratio, gras_ratio = 0.55, 0.25, 0.20
        elif objetivo == "perder":
            carb_ratio, prot_ratio, gras_ratio = 0.55, 0.40, 0.15

    carb_cal = carb_ratio * calorias_totales
    prot_cal = prot_ratio * calorias_totales
    gras_cal = gras_ratio * calorias_totales

    carb_g = carb_cal / 4
    prot_g = prot_cal / 4
    gras_g = gras_cal / 9

    resultado_str = (
        f"Objetivo para {objetivo} peso: {objetivo.capitalize()} peso\n"
        f"Gramos de carbohidratos: {round(carb_g)} g\n"
        f"Gramos de proteinas: {round(prot_g)} g\n"
        f"Gramos de grasa: {round(gras_g)} g"
    )

    macronutrientes_dict = {
        "Objetivo para": objetivo,
        "Carbohidratos (g)": round(carb_g),
        "Proteinas (g)": round(prot_g),
        "Grasas (g)": round(gras_g)
    }

    return resultado_str, macronutrientes_dict

#--------------------------------------------------------------

def gasto_calorico(genero,peso,altura,frec_ejer,edad,y_pred_kcal):
    if frec_ejer <1:
        frec_ejer=1.2
    elif 1<=frec_ejer <3:
        frec_ejer=1.375
    elif 3<=frec_ejer <=5:
        frec_ejer=1.55
    elif frec_ejer >5:
        frec_ejer=1.725
    
    if genero==1:
        TMB_M=10 * peso + 6.25 * altura -(5 * edad )+ 5       #altura cm
        kcal_d = (TMB_M * frec_ejer) + y_pred_kcal
    else:
        TMB_F=10 * peso + 6.25 * altura -(5 * edad) -161      #altura cm
        kcal_d = (TMB_F * frec_ejer) + y_pred_kcal
    return kcal_d

#--------------------------------------------------------------

def train_evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("R2 score", model.score(X_test, y_test))
    print("R2 score train", model.score(X_train, y_train))
    print("MAE", mean_absolute_error(y_test, y_pred))
    print("MSE", mean_squared_error(y_test, y_pred))
    print("RMSE", mean_squared_error(y_test, y_pred) ** (1/2))
    sns.displot(y_pred - y_test)
    return model

#----------------------------------------------------------------
import re

def convertir_tiempo_a_decimal(tiempo):

    horas = 0
    minutos = 0

    # Buscar horas y minutos con expresiones regulares
    match_horas = re.search(r"(\d+)h", tiempo)
    match_minutos = re.search(r"(\d+)min", tiempo)

    if match_horas:
        horas = int(match_horas.group(1))
    if match_minutos:
        minutos = int(match_minutos.group(1))

    return horas + (minutos / 60)
#---------------------------------------
def objetivo(imc):
    if imc < 18.5:
        return ["mantener", "ganar"] 
    elif 18.5 <= imc < 25:
        return ["mantener", "ganar", "perder"]  
    else:
        return ["mantener", "perder"] 
#-----------------------------
def recomendaciones(imc):
    if imc < 18.5:
        
        return """**Objetivo Recomendable:** Ganar peso de manera saludable.

    **Nutrición:**  
    - Aumentar la ingesta calórica con alimentos nutritivos (unas 300 kcal diarias de las recomendadas como máximo para que sea progresivo).  
    - Incluir más proteínas (pollo, pescado, huevos, legumbres).  
    - Consumir grasas saludables (aguacate, frutos secos, aceite de oliva).  
    - Aumentar la frecuencia de comidas (5-6 al día).  

    **Ejercicio recomendado:**  
    - **Fuerza:** Priorizar entrenamiento con pesas para ganar masa muscular.  
    - **Cardio:** Moderado, no excesivo, para no quemar demasiadas calorías.

**Objetivo Mantener Peso:** Mantener un estilo de vida saludable.

    **Nutrición:**  
    - Balance entre proteínas, carbohidratos y grasas saludables.  
    - Evitar exceso de azúcares y ultraprocesados.  
    - Hidratarse bien (mínimo 2L de agua al día).  

    **Ejercicio recomendado:**  
    - **Fuerza:** 2-3 veces por semana para mantener tono muscular.  
    - **Cardio:** 3-5 veces por semana (puede incluir HIIT y ejercicios aeróbicos).  
    - **Movilidad:** Yoga o estiramientos para evitar lesiones."""

    elif 18.5 <= imc < 25:
        return """**Objetivo Recomendable:** Mantener un estilo de vida saludable.

    **Nutrición:**  
    - Balance entre proteínas, carbohidratos y grasas saludables.  
    - Evitar exceso de azúcares y ultraprocesados.  
    - Hidratarse bien (mínimo 2L de agua al día).  

    **Ejercicio recomendado:**  
    - **Fuerza:** 2-3 veces por semana para mantener tono muscular.  
    - **Cardio:** 3-5 veces por semana (puede incluir HIIT y ejercicios aeróbicos).  
    - **Movilidad:** Yoga o estiramientos para evitar lesiones.

**Objetivo:** Ganar peso de manera saludable.

    **Nutrición:**  
    - Aumentar la ingesta calórica con alimentos nutritivos (unas 300 kcal diarias de las recomendadas como máximo para que sea progresivo).  
    - Incluir más proteínas (pollo, pescado, huevos, legumbres).  
    - Consumir grasas saludables (aguacate, frutos secos, aceite de oliva).  
    - Aumentar la frecuencia de comidas (5-6 al día).  

    **Ejercicio recomendado:**  
    - **Fuerza:** Priorizar entrenamiento con pesas para ganar masa muscular.  
    - **Cardio:** Moderado, no excesivo, para no quemar demasiadas calorías.

**Objetivo :** Reducir peso de forma progresiva y saludable.

    **Nutrición:**  
    - Mantener un déficit calórico controlado (-300 kcal diarias de las recomendadas como máximo).  
    - Aumentar el consumo de vegetales, proteínas magras y fibra.  
    - Reducir ultraprocesados, refrescos y azúcares añadidos.  

    **Ejercicio recomendado:**  
    - **Cardio:** Priorizar ejercicios aeróbicos de bajo impacto (caminar, nadar, bicicleta).  
    - **Fuerza:** Fundamental para preservar masa muscular mientras se pierde grasa.  
    - **HIIT:** Incluir sesiones cortas y progresivas según la condición física."""

    else:
        return """**Objetivo Recomendable:** Reducir peso de forma progresiva, saludable y controlada.

    **Nutrición:**  
    - Mantener un déficit calórico controlado (-300 kcal diarias de las recomendadas como máximo).  
    - Aumentar el consumo de vegetales, proteínas magras y fibra.  
    - Reducir ultraprocesados, refrescos y azúcares añadidos.  

    **Ejercicio recomendado:**  
    - **Cardio:** Priorizar ejercicios aeróbicos de bajo impacto (caminar, nadar, bicicleta).  
    - **Fuerza:** Fundamental para preservar masa muscular mientras se pierde grasa.  
    - **HIIT:** Incluir sesiones cortas y progresivas según la condición física.

**Objetivo:** Mantener un estilo de vida saludable.

    **Nutrición:**  
    - Balance entre proteínas, carbohidratos y grasas saludables.  
    - Evitar exceso de azúcares y ultraprocesados.  
    - Hidratarse bien (mínimo 2L de agua al día).  

    **Ejercicio recomendado:**  
    - **Fuerza:** 2-3 veces por semana para mantener tono muscular.  
    - **Cardio:** 3-5 veces por semana (puede incluir HIIT y ejercicios aeróbicos).  
    - **Movilidad:** Yoga o estiramientos para evitar lesiones."""



