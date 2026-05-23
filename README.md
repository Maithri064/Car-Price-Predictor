# 🚗 Car Price Predictor

An end-to-end Machine Learning web application that predicts the resale value of used cars based on historical data. This project covers everything from raw data cleaning in **Jupyter Notebook** to a complete web deployment using **Flask** inside **PyCharm**.

---
## 📂 Project Structure

car_price_predictor/
│
├── templates/
│   └── index.html                # Premium Dark-Theme UI Dashboard

│
├── application.py                # Main Flask Server Backend

├── cleaned car.csv               # Cleaned Dataset exported from Jupyter

├── LinearRegressionModel.pkl     # Trained & Serialized ML Model Pipeline

├── Quikr predictor.ipynb        # Jupyter Notebook (Data Analysis & Training)

└── README.md                     # Project Documentation

## 🛠️ Tech Stack & Architecture
The project bridges interactive data science development with a web application structure:

Data Analysis & Modeling: Jupyter Notebook, Python 3.8+, Pandas, NumPy, Scikit-Learn

Backend Web Framework: Flask, Flask-CORS

Frontend Design: HTML5, Bootstrap 4, JavaScript (AJAX asynchronous processing)

Model Serialization: Pickle

## 🔄 Project Workflow
1. Data Cleaning & Model Training (Jupyter Notebook)
All data exploration and model engineering are contained inside Quikr predictor.ipynb:

Data Prep: Handled missing data, filtered out severe vehicle pricing outliers, and standardized text strings.

Pipeline Creation: Used Scikit-Learn's ColumnTransformer and OneHotEncoder to encode categorical elements (name, company, fuel_type).

Model Training: Fitted a Linear Regression model inside an estimator pipeline to automate future data transforms.

Serialization: Exported the completed pipeline object directly into LinearRegressionModel.pkl.

2. Production Backend Deployment (PyCharm & Flask)

The model is served dynamically by application.py:

Automatically extracts unique labels from cleaned car.csv to cleanly populate user selectors.

Features a dedicated POST network route (/predict) to instantly ingest frontend form details, map strings cleanly into a target Pandas DataFrame, and calculate exact valuations using the pre-loaded Pickle pipeline.

3. Dynamic User Dashboard (HTML/JS)

Interactive UI: A dark-mode user layout featuring custom focused form behaviors and smooth visual state scaling.

Dependent Dropdowns: Built-in JavaScript event management automatically scans selecting a company (e.g., Audi) to instantly match and refresh only appropriate sub-models available for selection.

Zero-Refresh Performance: Leverages native AJAX asynchronous operations, keeping form elements locked in place while returning data calculations securely from the server.


<img width="1316" height="632" alt="car predictor" src="https://github.com/user-attachments/assets/35fb17de-ccf6-4e73-a53a-1b19545cc51b" />



