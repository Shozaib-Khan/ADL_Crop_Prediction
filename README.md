# 🌾 Crop Recommendation System

An intelligent crop recommendation web application that uses machine learning to suggest the best crops based on soil and climate conditions. Users can input values such as nitrogen, phosphorus, temperature, humidity, and rainfall to receive accurate crop predictions from trained models.

---

## 📌 Overview

This system is built using:

- **Frontend**: HTML and CSS  
- **Backend**: Flask (Python)  
- **Machine Learning Models**: Random Forest, Decision Tree, K-Nearest Neighbors  
- **Dataset**: Crop Recommendation Dataset from Kaggle  

### Users Can:

- Enter input parameters related to soil and environment  
- Choose an ML model (RF, DT, KNN)  
- View the top 3 crop recommendations with prediction probabilities  
- See a summary of their input data  

---

## ⚙️ Features

### ✅ Technical Features

- Flask-based Python backend  
- ML models trained using scikit-learn  
- HTML/CSS frontend with responsive design  
- Models saved as pickle files for reuse  

### 🌱 User Features

- Crop prediction based on environmental factors  
- View top 3 predictions with probabilities  
- Choose which ML model to use  
- Clean and mobile-friendly UI  

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.8 or later  
- pip (Python package installer)

### 🔧 Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
   cd crop-recommendation-system
``

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application

   ```bash
   python app.py
   ```
4. Open your browser and go to
   `http://127.0.0.1:5000/`

> **Note**: If the trained models are not found in the `models/` directory, they will be automatically trained on the first run.

---

## 🧠 ML Models and Accuracy

| Model               | Accuracy |
| ------------------- | -------- |
| Random Forest       | \~95%    |
| Decision Tree       | \~88%    |
| K-Nearest Neighbors | \~86%    |

---

## 🌐 Routes

| Route      | Method | Description                           |
| ---------- | ------ | ------------------------------------- |
| `/`        | GET    | Home page with input form             |
| `/predict` | POST   | Predicts crop using selected ML model |

---

## 📄 License

This project is licensed under the **MIT License**.
© 2025 Shozaib-Khan

---

## 📫 Contact

* **Email**: [equihealthh@gmail.com](mailto:equihealthh@gmail.com)
* **GitHub**: [https://github.com/Shozaib-Khan](https://github.com/Shozaib-Khan)

---

## 🌱 Future Enhancements

* Add charts to compare model predictions
* Support ensemble model prediction
* Implement user login and prediction history
* Redesign frontend using React or Vue
* Deploy app to a cloud platform like Vercel or Render

```

Let me know if you'd like it saved as a `.md` file or need a downloadable version!
```
