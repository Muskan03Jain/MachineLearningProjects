import pandas as pd
import numpy as np
import joblib
import streamlit as st

model= r"C:\Users\Lenovo\Muskan\Ml\final project\HeartDisease.pkl"
loaded_model=joblib.load(model)
 

st.header("Heart Disease Priction")

sex=st.selectbox("Select the Gender",("Male","Female"))
sex_dict={"Male":1,"Female":0}
sex=sex_dict[sex]

Age= st.number_input("Enter Age")

currentSmoker= st.selectbox("Do you smoke?",("Yes","No"))
currentSmoker_dict={"Yes":1,"No":0}
currentSmoker=currentSmoker_dict[currentSmoker]

cigsPerDay=st.number_input("Enter the consuption of cigrets per day")

BPMeds=st.selectbox("Currently on Blood Pressure Medication",("Yes","No"))
BPMeds_dict={"Yes":1,"No":0}
BPMeds=BPMeds_dict[BPMeds]

prevalentStroke=st.selectbox("previously had any heart stroke",("Yes","No"))
prevalentStroke_dict={"Yes":1,"No":0}
prevalentStroke=prevalentStroke_dict[prevalentStroke]

prevalentHyp=st.selectbox("Having Hypertention Issue",("Yes","No"))
prevalentHyp_dict={"Yes":1,"No":0}
prevalentHyp=prevalentHyp_dict[prevalentHyp]

diabetes=st.selectbox("having diabetes",("Yes","No"))
diabetes_dict={"Yes":1,"No":0}
diabetes=diabetes_dict[diabetes]

totChol=st.number_input("Enter total cholestrol level ")

sysBP=st.number_input("Enter systolic blood pressure")

diaBP=st.number_input("Enter diastolic bood pressure")

BMI=st.number_input("Enter your Body Mass Index")

heartRate	= st.number_input("Enter Heart Rate")

glucose= st.number_input("Enter Glucose Level")

array=np.array([[sex,Age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])

button=st.button("Submit")

if button:
      result = loaded_model.predict(array)
      if result==0:
            st.info("No")
      else:
            st.info("Yes")

      
