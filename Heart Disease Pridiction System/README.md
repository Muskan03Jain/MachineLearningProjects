---

# Heart Disease Prediction Project

This project is aimed at predicting the **10-year risk of coronary heart disease (CHD)** based on various **demographic**, **behavioral**, and **medical** risk factors. The dataset is sourced from the **Framingham Heart Study** and includes the following attributes:

## Dataset: `framingham.csv`

### Attributes
- **Demographic:**
  - `Sex`: Male or Female (Nominal)
  - `Age`: Age of the patient (Continuous)
  
- **Behavioral:**
  - `Current Smoker`: Whether the patient is a current smoker (Nominal)
  - `Cigs Per Day`: Number of cigarettes smoked per day (Continuous)
  
- **Medical History:**
  - `BP Meds`: Whether the patient is on blood pressure medication (Nominal)
  - `Prevalent Stroke`: Previous stroke history (Nominal)
  - `Prevalent Hyp`: Hypertension status (Nominal)
  - `Diabetes`: Diabetes status (Nominal)
  
- **Medical (Current):**
  - `Tot Chol`: Total cholesterol level (Continuous)
  - `Sys BP`: Systolic blood pressure (Continuous)
  - `Dia BP`: Diastolic blood pressure (Continuous)
  - `BMI`: Body Mass Index (Continuous)
  - `Heart Rate`: Heart rate (Continuous)
  - `Glucose`: Glucose level (Continuous)

- **Target Variable:**
  - `10 year risk of CHD`: Binary target (1 = Yes, 0 = No)

---

## Project Tasks

### 1. Data Exploration & Statistical Measures
- Explored the dataset and calculated various statistical measures to understand the distribution and relationships between variables.

### 2. Algorithm Identification
- Chose the following algorithms for building the prediction model:
  - **Logistic Regression**
  - **Decision Tree**
  - **Random Forest**

### 3. Data Preprocessing
- Handled missing values, normalized continuous variables, and encoded categorical features.

### 4. Model Building
- Built models using:
  - **Logistic Regression**
  - **Decision Tree**
  - **Random Forest**

### 5. Model Evaluation
- Evaluated models using precision, recall, and F1 score to assess performance.

### 6. Model Comparison
- Performed comparative analysis to select the best model based on performance metrics. The Random Forest algorithm was chosen for its balance of precision and recall.

### 7. Model Saving
- Saved the trained model using the `joblib` library into the file `HeartDisease.pkl`.

### 8. Streamlit Web Application
- Built an interactive web application using **Streamlit** to allow users to input patient data and predict the 10-year risk of CHD.
  
---

## Files in the Repository

- **`streamlit.py`**: Contains the code for the Streamlit web application.
- **`HeartDisease.ipynb`**: Jupyter notebook with data exploration, preprocessing, model training, and evaluation.
- **`HeartDisease.pkl`**: The saved machine learning model for predicting heart disease.
- **`framingham.csv`**: The dataset used for training and evaluating the model.

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

This will launch a web app where users can input patient data to predict the risk of heart disease.

---

