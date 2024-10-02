
---

# Machine Learning Projects

This repository contains a collection of eight machine learning projects, each addressing different real-world scenarios using a variety of machine learning algorithms. These projects focus on building, evaluating, and deploying predictive models using Streamlit and machine learning techniques.

## Projects Overview

### 1. **Bank Customer Churn Prediction**
   - **Objective**: Predict customer churn in the banking industry.
   - **Algorithms**: Bagging, Boosting, KNN.
   - **Model**: Bagging model selected for its accuracy.
   - **Features**: Customer demographics, credit score, account balance, and more.

### 2. **Bike Rental Prediction System**
   - **Objective**: Predict bike rentals based on various features.
   - **Algorithm**: Pre-trained Linear Regression.
   - **Features**: Season, temperature, weather, humidity, windspeed, etc.
   - **Deployment**: Streamlit web application for user input and predictions.

### 3. **Heart Disease Prediction System**
   - **Objective**: Predict the 10-year risk of coronary heart disease (CHD).
   - **Algorithms**: Logistic Regression, Decision Tree, Random Forest.
   - **Features**: Demographic, behavioral, and medical risk factors.
   - **Model Selection**: Random Forest chosen for best performance.

### 4. **Household Income Analysis**
   - **Objective**: Predict annual household income based on socioeconomic factors.
   - **Algorithms**: XGBoost, Decision Tree, Linear Regression.
   - **Model Selection**: XGBoost chosen for lowest error metrics (MSE, RMSE, R²).

### 5. **Iris Species Classification**
   - **Objective**: Classify Iris flower species (Setosa, Versicolor, Virginica).
   - **Algorithm**: K-Nearest Neighbors (KNN).
   - **Features**: Sepal and petal measurements.
   - **Deployment**: Streamlit application for species prediction.

### 6. **Loan Eligibility Checking System**
   - **Objective**: Predict loan approval based on payment history and credit score.
   - **Algorithm**: Decision Tree.
   - **Features**: Initial payment, last payment, credit score.
   - **Deployment**: Streamlit app for interactive loan eligibility checking.

### 7. **Medical Insurance Cost Prediction**
   - **Objective**: Predict medical insurance costs based on demographic and health data.
   - **Algorithm**: Linear Regression.
   - **Features**: Age, BMI, number of children, smoking status, region.
   - **Deployment**: Streamlit application for cost prediction.

### 8. **Titanic Survival Prediction**
   - **Objective**: Predict Titanic passenger survival based on demographic and travel data.
   - **Algorithm**: Logistic Regression.
   - **Features**: Age, sex, ticket class, family size.
   - **Deployment**: Streamlit web application for survival prediction.

## Repository Structure

```
machineLearningProjects/
│
├── BankCustomerChurn/
│   ├── BankChurn.ipynb
│   ├── streamlit.py
│   ├── BankCustomerChurn.pkl
│   └── ChurnModeling.csv
│
├── BikeRentPrediction/
│   ├── BikeRent.ipynb
│   ├── streamlit.py
│   ├── BikeRentalModel.pkl
│   └── BikeRentalData.csv
│
├── HeartDiseasePrediction/
│   ├── HeartDisease.ipynb
│   ├── streamlit.py
│   ├── HeartDisease.pkl
│   └── framingham.csv
│
├── HouseholdIncomePrediction/
│   ├── Income.ipynb
│   ├── streamlit.py
│   ├── HouseholdIncomeModel.pkl
│   └── regression_dataset.csv
│
├── IrisSpeciesClassification/
│   ├── IrisClassification.ipynb
│   ├── streamlit.py
│   ├── IrisModel.pkl
│   └── iris.csv
│
├── LoanEligibility/
│   ├── LoanEligibility.ipynb
│   ├── streamlit.py
│   ├── LoanEligibilityModel.pkl
│   └── LoanData.csv
│
├── MedicalInsuranceCost/
│   ├── InsuranceCost.ipynb
│   ├── streamlit.py
│   ├── MedicalInsuranceModel.pkl
│   └── InsuranceData.csv
│
├── TitanicSurvivalPrediction/
│   ├── TitanicSurvival.ipynb
│   ├── streamlit.py
│   ├── TitanicModel.pkl
│   └── titanic.csv
└── README.md
```

## How to Run the Projects

1. Clone the repository:
   ```
   git clone https://github.com/your-username/machineLearningProjects.git
   ```

2. Navigate to each project directory and run the Streamlit app:
   ```
   cd BankCustomerChurn
   streamlit run streamlit.py
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Key Technologies
- **Programming Language**: Python
- **Libraries**: NumPy, Pandas, Scikit-learn, XGBoost, Streamlit, Matplotlib, Seaborn
- **Deployment**: Streamlit Web Apps

---
