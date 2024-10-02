import pandas as pd
import numpy as np
import joblib
import streamlit as st

#make sure the below path of the model.pkl is correct according to your computer 
insurance_model_pkl = r"C:\Users\Lenovo\Muskan\Ml\github assignment\Machine-Learning-Projects\Linear_Regression\Medical_Insurance\model.pkl"
loaded_model = joblib.load(insurance_model_pkl)

st.header("Medical Insurance")

age=st.number_input("Enter the Age ")
bmi=st.number_input("Enter the  bmi")
sex = st.selectbox("Enter the sex", ("Male", "Female"))
sex_dict={"Male":0, "Female": 1,}
sex=sex_dict[sex]

children=st.number_input("Enter the number of children")

smoke = st.selectbox("do you smoke", ("Yes", "No"))
smoke_dict={"Yes":0, "No": 1,}
smoke=smoke_dict[smoke]

region = st.selectbox("which region", ("southwest", "southeast","northwest","northeast"))
region_dict={"southwest":0, "southeast":1,"northwest":2,"northeast":3}
region=region_dict[region]
X_new = np.array([[age,bmi,sex,children,smoke,region]])

button = st.button("Submit")

if button:

    result = loaded_model.predict(X_new)
    result=np.round(result[0])

    st.info("Amount of Insurance Predicted : " + str(result))
