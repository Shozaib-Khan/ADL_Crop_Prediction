# model.py
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
def load_data():
    df = pd.read_csv('data/Crop_recommendation.csv')
    return df

def preprocess_data(df):
    # Shuffle the dataset to remove any order effects
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Features and target
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    return X_train, X_test, y_train, y_test

def train_models():
    # Load and preprocess data
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # Train Random Forest model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_pred)
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    
    # Train Decision Tree model
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    dt_pred = dt_model.predict(X_test)
    dt_accuracy = accuracy_score(y_test, dt_pred)
    print(f"Decision Tree Accuracy: {dt_accuracy:.4f}")
    
    # Train KNN model
    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    knn_pred = knn_model.predict(X_test)
    knn_accuracy = accuracy_score(y_test, knn_pred)
    print(f"KNN Accuracy: {knn_accuracy:.4f}")
    
    # Save models
    with open('models/rf_model.pkl', 'wb') as f:
        pickle.dump(rf_model, f)
    
    with open('models/dt_model.pkl', 'wb') as f:
        pickle.dump(dt_model, f)
    
    with open('models/knn_model.pkl', 'wb') as f:
        pickle.dump(knn_model, f)
    
    # Get unique crop labels
    crop_labels = df['label'].unique().tolist()
    with open('models/crop_labels.pkl', 'wb') as f:
        pickle.dump(crop_labels, f)
    
    return rf_accuracy, dt_accuracy, knn_accuracy

if __name__ == "__main__":
    train_models()
