from sklearn.metrics import mean_squared_error,mean_absolute_error

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

def calcular_macronutrientes(calorias_totales):
    carb_cal = 0.50 * calorias_totales
    prot_cal = 0.35 * calorias_totales
    gras_cal = 0.15 * calorias_totales

    carb_g = carb_cal / 4
    prot_g = prot_cal / 4
    gras_g = gras_cal / 9

    return f"CH_g:{carb_g},P_g: {prot_g}, G_g:{gras_g}"

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

    
