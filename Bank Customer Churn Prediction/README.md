
---

# Bank Customer Churn Prediction

This project aims to predict customer churn in the banking industry by using machine learning models such as **Bagging**, **Boosting**, and **KNN algorithms**. The dataset used for this project contains information on bank customers and whether they have exited (churned) from the bank. The goal is to create, evaluate, and compare multiple machine learning models to find the best performing model for predicting customer churn.

## Dataset Description

The dataset `Churn Modeling.csv` consists of the following attributes:

- **Customer ID**: A unique identifier for each customer.
- **Surname**: The customer's surname or last name.
- **Credit Score**: A numerical value representing the customer's credit score.
- **Geography**: The country where the customer resides (France, Spain, or Germany).
- **Gender**: The customer's gender (Male or Female).
- **Age**: The customer's age.
- **Tenure**: The number of years the customer has been with the bank.
- **Balance**: The customer's account balance.
- **NumOfProducts**: The number of bank products the customer uses (e.g., savings account, credit card).
- **HasCrCard**: Whether the customer has a credit card (1 = yes, 0 = no).
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no).
- **EstimatedSalary**: The estimated salary of the customer.
- **Exited**: Whether the customer has churned (1 = yes, 0 = no).

## Project Structure

- **Churn Modeling.csv**: The dataset used for model training and evaluation.
- **Bank Churn.ipynb**: The Jupyter Notebook containing the entire data exploration, preprocessing, and machine learning model creation process.
- **Bank Customer Churn.pkl**: The saved best model for customer churn prediction.
- **streamlit.py**: The Python script for the Streamlit web app.

## Tasks and Workflow

1. **Explore the Data and Calculate Statistical Measures**:
    - Data exploration and understanding of features.
    - Calculating measures like mean, median, mode, and standard deviation to assess the distribution and characteristics of the dataset.

2. **Identify the Algorithm**:
    - Selected algorithms for modeling include:
      - **Bagging**: To reduce variance and improve model accuracy.
      - **Boosting**: To improve weak learners through a sequential process.
      - **KNN (K-Nearest Neighbors)**: To classify the data based on proximity.

3. **Preprocess the Data**:
    - Handled missing data, encoded categorical variables (e.g., Geography and Gender).
    - Standardized/normalized numerical features for better model performance.
    - Split the data into training and testing sets for model evaluation.

4. **Create Machine Learning Models**:
    - Created three machine learning models using Bagging, Boosting, and KNN techniques.
    - Trained and evaluated each model.

5. **Evaluate Precision, Recall, and F1 Score**:
    - Evaluated the models based on precision, recall, F1 score, and accuracy to understand their performance.

6. **Comparative Analysis**:
    - Performed a comparative analysis of the models based on their performance metrics (precision, recall, F1 score).
    - Selected the best model for deployment (e.g., **Bagging model**, due to its high accuracy and generalization capability).

7. **Save the Best Model**:
    - The best performing model (Bagging model) was saved as `Bank Customer Churn.pkl`.

8. **Create a Streamlit Web App**:
    - A Streamlit app (`streamlit.py`) was built to allow users to input customer details and predict churn probability using the saved model.

## How to Run the Project

### Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Streamlit App

To run the web app, use the following command:

```bash
streamlit run streamlit.py
```

The web app will allow you to input customer details (credit score, age, geography, etc.) and get a prediction on whether the customer is likely to churn or not.


The **Bagging model** was selected as the best model due to its superior performance across all metrics.

## Project Files

- **Churn Modeling.csv**: The dataset.
- **Bank Churn.ipynb**: Jupyter notebook for training the models.
- **Bank Customer Churn.pkl**: The saved best-performing model.
- **streamlit.py**: Python script for the Streamlit app.

---
