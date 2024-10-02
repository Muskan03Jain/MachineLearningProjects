# Titanic Survival Prediction System

This project predicts whether a passenger on the Titanic would have survived based on various input features using a Logistic Regression model. The project includes feature scaling, model training, and deployment using a Streamlit web application.

## Projects

### 1. Titanic Survival Prediction System

This project predicts the survival status of passengers aboard the Titanic based on features like class, sex, age, number of siblings/spouses aboard, number of parents/children aboard, fare, and port of embarkation.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/titanic-survival-prediction.git
   cd titanic-survival-prediction

##Install the required dependencies
streamlit run streamlit.py

##Usage

###Titanic Survival Prediction System
1)Once the Streamlit app is running, you will see a web interface.
2)Use the provided input fields to enter passenger details such as class, sex, age, number of siblings/spouses, fare, etc.
3)Click the "Submit" button to get the prediction for the survival status of the passenger.
Models
4)The project uses a Logistic Regression model with scaled features. The following files are included:

**scaler.pkl:** The saved scaler used to normalize the features.
**Titanic_model.pkl:** The pre-trained Logistic Regression model.
Files
**streamlit.py:** The Streamlit application script for Titanic Survival Prediction.
**Scaler.ipynb:** Jupyter notebook for feature scaling.
**Logistic.ipynb:** Jupyter notebook for training the Logistic Regression model.
**scaler.pkl:** The saved scaler model.
**Titanic_model.pkl:** The pre-trained Logistic Regression model.
**data/train.csv:** The dataset used for training.
**requirements.txt:** List of required Python packages.
**README.md:** Project documentation.

###Dataset
The dataset used for this project is the Titanic dataset (train.csv), which includes the following features:

Pclass: Passenger class (1st, 2nd, 3rd)
Sex: Gender of the passenger
Age: Age of the passenger
SibSp: Number of siblings/spouses aboard the Titanic
Parch: Number of parents/children aboard the Titanic
Fare: Fare paid by the passenger
Embarked: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
Survived: Survival status (0 = No, 1 = Yes) [This is the target variable]
Contributing
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

###License
This project is licensed under the MIT License - see the LICENSE file for details.

###Acknowledgments
This project was developed using Streamlit and scikit-learn.
Special thanks to the authors of the Titanic dataset and tools used in this project.
