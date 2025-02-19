import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from utils import train_evaluate_model

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import  LinearRegression, Ridge
from sklearn.metrics import mean_squared_error,mean_absolute_error

df=pd.read_csv("../data/df_clasi.csv")
X=df[['Age', 'Height', 'Weight', 'family_with_overweight', 'Alcohol','Andar_bici','Control_kcal', 'FastFood',"Male"]]
y= df["BMI"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pol_2 = PolynomialFeatures(degree=2)

X_train_pol2 = pol_2.fit_transform(X_train)
X_test_pol2 = pol_2.transform(X_test)

model_4 = train_evaluate_model(LinearRegression(), X_train_pol2, y_train, X_test_pol2, y_test)
model_4

# Guardar el transformador PolynomialFeatures
with open("../modelos/pol2_transform_ob.pkl", "wb") as pol_transf_ob:
    pickle.dump(pol_2, pol_transf_ob)

with open("../modelos/pol2_ob.pkl", "wb") as model_pol2_ob:
    pickle.dump(model_4, model_pol2_ob)

X_ejer_pol2 = pol_2.transform(X_test)
y_pred_ejer_pol2 = np.round(model_4.predict(X_ejer_pol2),2)


