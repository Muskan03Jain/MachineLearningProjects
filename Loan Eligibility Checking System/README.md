
# Loan Prediction System

This project is a machine learning application that predicts loan approval based on initial payment, last payment, and credit score. The model is built using a decision tree algorithm and is deployed using Streamlit to provide an interactive interface.

## Project Structure

The project contains the following files:

- **`loan_data.csv`**: The dataset used to train the decision tree model. It includes features such as initial payment, last payment, credit score, and loan approval status.
  
- **`loan_model.pkl`**: The pre-trained decision tree model saved as a pickle file. This model is used to predict loan approval based on the input features.

- **`decision_tree.ipynb`**: The Jupyter Notebook containing the code for data processing, model training, and evaluation. This notebook provides a step-by-step explanation of how the decision tree model was developed.

- **`streamlit.py`**: The Streamlit application file that provides an interface for users to input their data and receive predictions on loan approval.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/loan-prediction-system.git
    cd loan-prediction-system
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit.py
    ```

## Usage

Once the Streamlit app is running, you can interact with it through a web interface:

- **Initial Payment:** Enter the initial payment amount.
- **Last Payment:** Enter the last payment amount.
- **Credit Score:** Enter the credit score.
- **Submit:** Click the "Submit" button to get the loan prediction result.

The model will predict whether the loan will be approved based on the provided inputs.

## Model

The decision tree model used in this application is trained on the `loan_data.csv` dataset. The model's primary features include the initial payment, last payment, and credit score. The model is stored in the `loan_model.pkl` file and is loaded into the Streamlit app for making predictions.

## Files

- **`loan_data.csv`**: Dataset used for training the model.
- **`loan_model.pkl`**: Pre-trained decision tree model.
- **`decision_tree.ipynb`**: Jupyter Notebook for model training.
- **`streamlit.py`**: Streamlit application for loan prediction.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was developed using Streamlit and scikit-learn. Special thanks to the authors of the tools and datasets used in this project.
