import pandas as pd
import numpy as np
import streamlit as st
import joblib

model=r"C:\Users\Lenovo\Muskan\Ml\final project\ass2\Bank Customer Churn.pkl"
loaded_model=joblib.load(model)

st.header("Bank Customer Churn Prediction")

CreditScore = st.number_input("Enter Credit Score",)

Geography = st.selectbox("Select your geographical location",("France","Spain","Germany"))
Geography_dict={"France":0,"Spain":1,"Germany":2}
Geography=Geography_dict[Geography]

Gender=st.selectbox("Select your Gender",("Male","Female"))
Gender_dict={"Male":0,"Female":1}
Gender=Gender_dict[Gender]

Age=st.number_input("Enter your age")

Tenure=st.number_input("How many years completed with the bank")

Balance=st.number_input("Enter your bank balance")

NumOfProducts=st.number_input("Enter the number of bank products uses (e.g., savings account, credit card)")

HasCrCard = st.selectbox("Have Credit Card",("Yes","No"))
HasCrCard_dict={"Yes":1,"No":0}
HasCrCard=HasCrCard_dict[HasCrCard]

IsActiveMember = st.selectbox("Is Active Member",("Yes","NO"))
IsActiveMember_dict={"Yes":1,"No":0}
IsActiveMember=IsActiveMember_dict[IsActiveMember]

EstimatedSalary=st.number_input("Enter estimate salary")

X =np.array([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

button=st.button("Submit")

if button:
      result=loaded_model.predict(X)
      if result==0:
            st.info("No")
      else:
          st.info("Yes")   
      
      
