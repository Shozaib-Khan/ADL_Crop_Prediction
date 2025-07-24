Crop Recommendation System
An intelligent crop recommendation web application that uses machine learning to suggest the best crops based on soil and climate conditions. Users can input values such as nitrogen, phosphorus, temperature, humidity, and rainfall to receive accurate crop predictions from trained models.

Overview
This system is built using:

Frontend: HTML and CSS

Backend: Flask (Python)

Machine Learning Models: Random Forest, Decision Tree, K-Nearest Neighbors

Dataset: Crop Recommendation Dataset from Kaggle

Users can:

Enter input parameters related to soil and environment

Choose an ML model (RF, DT, KNN)

View the top 3 crop recommendations with prediction probabilities

See a summary of their input data

Features
Technical Features:
Flask-based Python backend

ML models trained using scikit-learn

HTML/CSS frontend with responsive design

Models saved as pickle files for reuse

User Features:
Crop prediction based on environmental factors

View top 3 predictions with probabilities

Choose which ML model to use

Clean and mobile-friendly UI

Project Structure
app.py: Main Flask app that handles routing and prediction logic

model.py: Responsible for loading the dataset, preprocessing, training models, and saving them

models/: Directory containing saved .pkl files for each model

templates/: Contains HTML templates (index.html and result.html)

static/style.css: Styling for the web app

data/Crop_recommendation.csv: Dataset file (not included here)

requirements.txt: Python dependencies

LICENSE: Project license (MIT)

Getting Started
Prerequisites:
Python 3.8 or later

pip (Python package installer)

Installation:
Clone the repository

Navigate into the project directory

Install dependencies using pip install -r requirements.txt

Run the application with python app.py

Open a browser and visit http://127.0.0.1:5000/

Note: If the models are not already saved in the models/ folder, they will be automatically trained on the first run.

ML Models and Accuracy
Random Forest: ~95%

Decision Tree: ~88%

K-Nearest Neighbors: ~86%

Routes
/ (GET): Home page with input form

/predict (POST): Processes input and returns crop recommendation

License
This project is licensed under the MIT License.
Copyright (c) 2025 Shozaib-Khan

Contact
Email: equihealthh@gmail.com
GitHub: https://github.com/Shozaib-Khan

Future Enhancements
Add charts to compare model predictions

Add ensemble prediction using multiple models

Implement user login and history tracking

Migrate to a React frontend for better UX

