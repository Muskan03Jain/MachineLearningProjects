import numpy as np
import pandas as pd
import joblib
import streamlit as st

model=r"C:\Users\Lenovo\Muskan\Ml\final project\ass3\Household Income Analysis.pkl"
loaded_model=joblib.load(model)

st.header("Household Income Prediction")
Age=st.number_input("Enter Age")

Education_Level=st.selectbox("Select Education level",("High School","Bachelor's","Master's","Doctorate"))
Education_Level_dict={"High School":0,"Bachelor's":1,"Master's":2,"Doctorate":3}
Education_Level=Education_Level_dict[Education_Level]

Occupation=st.selectbox("Select occupation",("Healthcare","Education","Technology","Finance","Others"))
Occupation_dict={"Healthcare":0,"Education":1,"Technology":2,"Finance":3,"Others":4}
Occupation=Occupation_dict[Occupation]

Number_of_Dependents=st.number_input("Enter the numbers of dependents")

Location=st.selectbox("Select the location type",("Urban","Suburban","Rural"))
Location_dict={"Urban":0,"Suburban":1,"Rural":2}
Location=Location_dict[Location]

Work_Experience=st.number_input("Enter numbers of years of work experience")

Marital_Status=st.selectbox("Select Maratial status",("Single","Married","Divorced"))
Marital_Status_dict={"Single":0,"Married":1,"Divorced":2}
Marital_Status=Marital_Status_dict[Marital_Status]

Employment_Status=st.selectbox("Select Employement status",("Full-time","Part-time","Self-employed"))
Employment_Status_dict={"Full-time":0,"Part-time":1,"Self-employed":2}
Employment_Status=Employment_Status_dict[Employment_Status]

Household_Size=st.number_input("Total number of individuals living in the household")

Homeownership_Status=st.selectbox("Select Homeownership status",("Own","Rent"))
Homeownership_Status_dict={"Own":0,"Rent":1}
Homeownership_Status=Homeownership_Status_dict[Homeownership_Status]

Type_of_Housing=st.selectbox("Type of housing" ,("Apartment","Single-family home","Townhouse"))
Type_of_Housing_dict={"Apartment":0,"Single-family home":1,"Townhouse":2}
Type_of_Housing=Type_of_Housing_dict[Type_of_Housing]

Gender=st.selectbox("Gender of the primary household member",("Male","Female"))
Gender_dict={"Male":0,"Female":1}
Gender=Gender_dict[Gender]

Primary_Mode_of_Transportation=st.selectbox("Primary mode of transportation used by the household member",("Car","Public transit","Biking","Walking"))
Primary_Mode_of_Transportation_dict={"Car":0,"Public transit":1,"Biking":2,"Walking":3}
Primary_Mode_of_Transportation=Primary_Mode_of_Transportation_dict[Primary_Mode_of_Transportation]

X=np.array([[Age,Education_Level,Occupation,Number_of_Dependents,Location,Work_Experience,Marital_Status,Employment_Status,Household_Size,Homeownership_Status,Type_of_Housing,Gender,Primary_Mode_of_Transportation]])

button=st.button("Submit")
if button:
      result = loaded_model.predict(X)
      result=np.round(result[0])

      st.info("Household salary of indivisual is : " + str(result))