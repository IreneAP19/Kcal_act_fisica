import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("../data/raw/ObesityDataSet_raw_and_data_sinthetic.csv")

df["Male"] = df["Gender"].map({"Male": 1, "Female": 0})
df=df.drop(columns="Gender")

df["BMI"]=df["Weight"]/(df["Height"])**2

df["family_with_overweight"]=df["family_history_with_overweight"].map({"yes":1,"no":0})
df=df.drop(columns="family_history_with_overweight")

df["Alcohol"]=df["CALC"].map({'no':0, 'Sometimes':1, 'Frequently':2, 'Always':3})
df=df.drop(columns="CALC")

#nos centramos en si se ejercita de alguna forma o depende de un medio de transporte
df["Andar_bici"]=df["MTRANS"].map({'Public_Transportation':0,'Automobile':0, 'Motorbike':0,'Walking':1,'Bike':1})
df=df.drop(columns="MTRANS")

#Nos vamos a centrar en si la persona pica o no entre horas, independientemente de la frecuencia, ya que no sabemos la cantidad que es lo realmente importante
df["Picoteo"]=df["CAEC"].map({'Sometimes':1, 'Frequently':1, 'Always':1, 'no':0})
df=df.drop(columns="CAEC")

df["Fumador"]=df["SMOKE"].map({'no':0,"yes":1})
df=df.drop(columns="SMOKE")

df["Control_kcal"]=df["SCC"].map({'no':0,"yes":1})
df=df.drop(columns="SCC")

df["FastFood"]=df["FAVC"].map({'no':0,"yes":1})
df=df.drop(columns="FAVC")

df["Age"]=df["Age"].astype(int)

#--------------------------------------

df2=pd.read_csv("../data/raw/data_test.csv")

df2["Male"] = df2["Gender"].map({"Male": 1, "Female": 0})
df2=df2.drop(columns="Gender")

df2 = pd.get_dummies(df2, columns=['Workout_Type'])
df2=df2.replace({True:1,False:0})

#---------------------------------------

df_kcal=pd.read_csv("../data/data_test.csv")

df_kcal["Male"] = df_kcal["Gender"].map({"Male": 1, "Female": 0})
df_kcal=df_kcal.drop(columns="Gender")

df_kcal = pd.get_dummies(df_kcal, columns=['Workout_Type'])
df_kcal=df_kcal.replace({True:1,False:0})