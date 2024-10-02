# Medical Insurance Prediction System

This project includes a Streamlit application for predicting medical insurance costs using a trained linear regression model. The model is based on various features such as age, sex, body mass index (BMI), number of children, smoking status, and region.

# Project Structure
The project contains the following files:


**app.py**: The Streamlit application file that provides the user interface for inputting data and receiving insurance cost predictions.


**model.pkl**: The trained linear regression model saved as a pickle file. This model predicts medical insurance costs based on input features.

**insurance.ipynb**: A Jupyter Notebook that contains the data processing and model training steps. This notebook demonstrates how the data was preprocessed, how the model was trained, and how the model was saved as a pickle file.

**insurance.csv**: The dataset used for training the model. This file contains data on age, sex, BMI, number of children, smoking status, region, and insurance charges.

**README.md**: This file, providing an overview of the project.
#Streamlit Application
The Streamlit application (app.py) allows users to input their data and get predictions for medical insurance costs. The application uses the trained model (model.pkl) to make these predictions.

# Data Processing and Model Training
The data processing and model training steps are documented in the insurance.ipynb Jupyter Notebook. This notebook includes:

**Loading the Data:** Importing the dataset and performing initial exploration.

**Data Cleaning:** Handling missing values and encoding categorical variables.

**Feature Scaling:** Normalizing the data to improve model performance.

**Model Training:** Training a linear regression model on the processed data.

**Model Evaluation**: Evaluating the model's performance using various metrics.

**Model Saving:** Saving the trained model as a pickle file (model.pkl).


