
# Household Income Prediction Project

This project simulates **household income prediction** based on various **demographic** and **socioeconomic** factors. The dataset includes multiple features that could influence annual household income. This project explores data relationships, builds predictive models, and evaluates their performance.

---

## Dataset: `regression_dataset.csv`

### Features
- **Age**: Age of the primary household member (18 to 70 years).
- **Education Level**: Highest education level attained (High School, Bachelor's, Master's, Doctorate).
- **Occupation**: Type of occupation (Healthcare, Education, Technology, Finance, Others).
- **Number of Dependents**: Number of dependents in the household (0 to 5).
- **Location**: Residential location (Urban, Suburban, Rural).
- **Work Experience**: Years of work experience (0 to 50 years).
- **Marital Status**: Marital status of the primary household member (Single, Married, Divorced).
- **Employment Status**: Employment status of the primary household member (Full-time, Part-time, Self-employed).
- **Household Size**: Total number of individuals living in the household (1 to 7).
- **Homeownership Status**: Homeownership status (Own, Rent).
- **Type of Housing**: Type of housing (Apartment, Single-family home, Townhouse).
- **Gender**: Gender of the primary household member (Male, Female).
- **Primary Mode of Transportation**: Primary mode of transportation used (Car, Public transit, Biking, Walking).
- **Annual Household Income**: Actual annual household income (in USD) derived from a combination of features with added noise.

---

## Project Tasks

### 1. Data Exploration & Statistical Analysis
- Explored the dataset and calculated various statistical measures to understand the distribution of features.

### 2. Algorithm Selection
- The following algorithms were used for building predictive models:
  - **XGBoost**
  - **Decision Tree**
  - **Linear Regression**

### 3. Data Preprocessing
- Handled missing values, performed feature encoding, normalized continuous variables, and prepared data for model training.

### 4. Model Building
- Trained models using:
  - **XGBoost**
  - **Decision Tree**
  - **Linear Regression**

### 5. Model Evaluation
- Evaluated models using the following metrics:
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **R-squared (R²) Score**

### 6. Model Comparison & Selection
- Performed comparative analysis to select the best model based on MSE, RMSE, and R² scores. The **XGBoost** model was chosen for its better performance and balance of error metrics.

### 7. Model Saving
- Saved the trained model using the `joblib` library into the file `HouseHoldIncome.pkl`.

### 8. Streamlit Web Application
- Built an interactive web application using **Streamlit** to allow users to input household data and predict the annual income.

---

## Files in the Repository

- **`streamlit.py`**: Contains the code for the Streamlit web application.
- **`Income.ipynb`**: Jupyter notebook with data exploration, preprocessing, model training, and evaluation.
- **`HouseHoldIncome.pkl`**: The saved machine learning model for predicting household income.
- **`regression_dataset.csv`**: The dataset used for training and evaluating the model.

---

## Usage

### 1. Clone the Repository
```bash
git clone <repo-link>
```

### 2. Install the Required Libraries
Use the following command to install the dependencies listed in the `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
To launch the web application, run the following command:
```bash
streamlit run streamlit.py
```

This will launch a web app where users can input household data and predict the annual income.
