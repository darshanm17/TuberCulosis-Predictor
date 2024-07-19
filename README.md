# Tuberculosis Predictor

Tuberculosis Predictor is a web application that allows users to upload X-ray images and predict the likelihood of tuberculosis using a Convolutional Neural Network (CNN) algorithm implemented with TensorFlow. The frontend is built with React, providing an intuitive interface for users to interact with the model.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [License](#license)
- [Contact](#contact)

## Features

- Upload X-ray images for tuberculosis prediction.
- Real-time prediction results.
- User-friendly interface built with React.
- Animated statistics display.
- Information about tuberculosis and its symptoms.

## Demo

You can try a live demo of the application [here](#).

## Installation

### Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/darshanm17/TuberCulosis_Predictor.git
   cd TuberCulosis_Predictor/backend
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Start the Flask server:
   ```bash
   flask run

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd ../Tb_Predictor_Frontend
2. Install the required dependencies:
   ```bash
   npm create vite@latest
   npm install axios
   npm install animate.css

3. Start the React development server:
   ```bash
   npm run dev

## Usage:
- Ensure the backend server is running.
- Navigate to the frontend directory and start the React development server.
- Open your browser and go to http://localhost:3000.
- Upload an X-ray image using the provided form and click on "Upload and Predict".
- View the prediction result and other relevant information.

## Technologies Used:
### Backend:
- Backend
- Python
- Flask
- TensorFlow
- Keras
  
### Frontend
- React
- Axios
- Animate.css

## Dataset
This project uses the Kaggle Chest X-ray Tuberculosis dataset, organized into three folders: train, test, and val.

Train: Contains the training data used to train the CNN model.
Test: Contains the test data used to evaluate the model's performance.
Val: Contains the validation data used to tune the model's hyperparameters.
You can download the dataset from [here](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset).
