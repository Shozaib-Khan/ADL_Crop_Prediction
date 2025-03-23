# app.py
from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load models
def load_models():
    with open('models/rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    
    with open('models/dt_model.pkl', 'rb') as f:
        dt_model = pickle.load(f)
    
    with open('models/knn_model.pkl', 'rb') as f:
        knn_model = pickle.load(f)
    
    with open('models/crop_labels.pkl', 'rb') as f:
        crop_labels = pickle.load(f)
    
    return rf_model, dt_model, knn_model, crop_labels

# Load models if they exist, otherwise train them
if not os.path.exists('models/rf_model.pkl'):
    from model import train_models
    train_models()

rf_model, dt_model, knn_model, crop_labels = load_models()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [
        float(request.form['nitrogen']),
        float(request.form['phosphorus']),
        float(request.form['potassium']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]
    
    # Convert to numpy array
    features_array = np.array([features])
    
    # Get selected model
    model_name = request.form['model']
    
    # Make prediction based on selected model
    if model_name == 'rf':
        prediction = rf_model.predict(features_array)[0]
        model_display_name = "Random Forest"
    elif model_name == 'dt':
        prediction = dt_model.predict(features_array)[0]
        model_display_name = "Decision Tree"
    else:  # knn
        prediction = knn_model.predict(features_array)[0]
        model_display_name = "K-Nearest Neighbors"
    
    # Get prediction probabilities for the selected model
    if model_name == 'rf':
        probabilities = rf_model.predict_proba(features_array)[0]
    elif model_name == 'dt':
        probabilities = dt_model.predict_proba(features_array)[0]
    else:  # knn
        probabilities = knn_model.predict_proba(features_array)[0]
    
    # Get top 3 predictions
    top_indices = np.argsort(probabilities)[-3:][::-1]
    top_crops = [rf_model.classes_[i] for i in top_indices]
    top_probs = [probabilities[i] * 100 for i in top_indices]
    
    # Prepare results
    results = {
        'prediction': prediction,
        'model_name': model_display_name,
        'top_crops': top_crops,
        'top_probs': top_probs,
        'input_features': {
            'Nitrogen': features[0],
            'Phosphorus': features[1],
            'Potassium': features[2],
            'Temperature': features[3],
            'Humidity': features[4],
            'pH': features[5],
            'Rainfall': features[6]
        }
    }
    
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
