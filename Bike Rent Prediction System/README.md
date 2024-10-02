
# Bike Rental Prediction System

This repository contains a Streamlit application for predicting bike rentals based on various input features. The model used for predictions is a pre-trained linear regression model.

## Description

This project is designed to predict the total number of bike rentals based on user input for various features such as season, month, holiday status, weekday, working day status, weather situation, temperature, apparent temperature, humidity, and windspeed. The application uses a pre-trained model saved as a pickle file to make predictions.

## Features

- **Season**: Select from Spring, Summer, Autumn, or Winter.
- **Month**: Select from January to December.
- **Holiday Status**: Select whether it's a public holiday or not.
- **Weekday**: Select the day of the week.
- **Working Day Status**: Select whether it's a working day or not.
- **Weather Situation**: Select the weather situation from Clear, Mist/Cloudy, Light Rainfall/Snowfall, or Hailstorm.
- **Temperature**: Input the temperature (normalized).
- **Apparent Temperature**: Input the apparent temperature (normalized).
- **Humidity**: Input the humidity level (normalized).
- **Windspeed**: Input the windspeed (normalized).
 

## Usage

1. Once the Streamlit app is running, you will see a web interface.
2. Use the provided input fields to select or input the required features.
3. Click the "Submit" button to get the prediction for the total number of bike rentals.

## Model

The model used in this application is a pre-trained linear regression model saved as a pickle file (`model.pkl`). This file is included in the repository.

## Files

- **app.py**: The main Streamlit application script.
- **requirements.txt**: List of required Python packages.
- **model.pkl**: The pre-trained model file.
- **bike_rental_LR.ipynb**: Jupyter Notebook containing the data processing and model training steps.
- **daily-bike-shared.csv**: Dataset used for training the model.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was developed using Streamlit. Special thanks to the authors of the datasets and tools used in this project.

