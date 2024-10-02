import pandas as pd
import numpy as np
import joblib
import streamlit as st

loan=r"C:\Users\Lenovo\Muskan\Ml\Machine-Learning-Projects\Decision_Tree\Loan_Classification\loan_model.pkl"
loaded_model=joblib.load(loan)

st.header("Loan Prediction")

initial=st.number_input("Enter the initial payment")
last=st.number_input("Enter the last payemnt")
score=st.number_input("Enter the credit score")

data=np.array([[initial,last,score]])
button=st.button("Submit")
if button:
      result =loaded_model.predict(data)
      st.info(result)
       