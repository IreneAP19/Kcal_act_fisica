import pandas as pd
import numpy as np
import pickle
from utils import train_evaluate_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import  LinearRegression


df2=pd.read_csv("../data/df_train_kcal.csv")

X1= df2[['Age', 'Weight (kg)', 'Height (m)','Session_Duration (hours)','Fat_Percentage','Workout_Type_Cardio',
       'Workout_Type_HIIT', 'Workout_Type_Strength', 'Workout_Type_Yoga',"Male","BMI"]]
y1= df2["Calories_Burned"]

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

pol_2= PolynomialFeatures(degree=2)

X_train_pol2 = pol_2.fit_transform(X1_train)
X_test_pol2 = pol_2.transform(X1_test)

model_5 = train_evaluate_model(LinearRegression(), X_train_pol2, y1_train, X_test_pol2, y1_test)
model_5

# Guardar el transformador PolynomialFeatures
with open("../modelos/pol2_transform_ejer.pkl", "wb") as pol_transf_ejer:
    pickle.dump(pol_2, pol_transf_ejer)

with open("../modelos/pol2_ejer.pkl", "wb") as model_pol2_ejer:
    pickle.dump(model_5, model_pol2_ejer)

df_kcal=pd.read_csv("../data/df_test_kcal.csv")

X_kcl= df_kcal[['Age', 'Weight (kg)', 'Height (m)','Session_Duration (hours)','Fat_Percentage','Workout_Type_Cardio',
       'Workout_Type_HIIT', 'Workout_Type_Strength', 'Workout_Type_Yoga',"Male","BMI"]]

X_kcl_pol2 = pol_2.transform(X_kcl)
y_pred_kcal_pol2 = model_5.predict(X_kcl_pol2)

y_pred_kcal_pol2=np.round(y_pred_kcal_pol2)
