import pandas as pd
import numpy as np
import joblib
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Load the model and the scaler
model_pkl = r'C:\Users\Lenovo\Muskan\Ml\Machine-Learning-Projects\Logistic_Regression\Titanic_model.pkl'
loaded_model = joblib.load(model_pkl)

scaler_pkl = r'C:\Users\Lenovo\Muskan\Ml\Machine-Learning-Projects\Logistic_Regression\scaler.pkl'
scaler = joblib.load(scaler_pkl)  # Assuming you've saved the scaler

st.header("Titanic Survival Prediction System")

# Inputs
Pclass = st.number_input("Enter the class type of passenger")

Sex = st.selectbox("Enter the Sex", ('Male', 'Female'))
Sex_dict = {'Male': 0, 'Female': 1}
Sex = Sex_dict[Sex]

Age = st.number_input("Enter the Age")
Fare = st.number_input("Enter the Fare")

# Normalize Age and Fare using the scaler
Age_normalized = scaler.transform([[Age]])[0][0]  # Normalize age
Fare_normalized = scaler.transform([[Fare]])[0][0]  # Normalize fare

SibSp = st.number_input("Enter number of siblings/spouses aboard")
Parch = st.number_input("Enter number of parents/children aboard")

Embarked = st.selectbox("Enter the port of embarkation", ('C', 'Q', 'S'))
Embarked_dict = {'C': 0, 'Q': 1, 'S': 2}
Embarked = Embarked_dict[Embarked]

# Prepare the input array
input_data = np.array([[Pclass, Sex, Age_normalized, SibSp, Parch, Fare_normalized, Embarked]])

# Prediction
if st.button("Predict"):
    prediction = loaded_model.predict(input_data)
    result = "Survived" if prediction == 1 else "Did not survive"
    st.write(f"The person would have {result}")
