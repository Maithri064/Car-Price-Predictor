from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model and data safely
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    # Extract unique values for the dropdowns
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    # Send the variables to your HTML template
    return render_template('index.html',
                           companies=companies,
                           car_models=car_models,
                           years=year,
                           fuel_types=fuel_type)


# @app.route('/predict', methods=['POST'])
# @cross_origin()
# def predict():
#     try:
#         # 1. Get data from the form safely
#         company = request.form.get('company')
#         car_model = request.form.get('car_models')
#
#         # 2. Convert incoming text data to integers to match model requirements
#         year = int(request.form.get('year'))
#         kms_driven = int(request.form.get('kilo_driven'))
#         fuel_type = request.form.get('fuel_type')
#
#         # 3. Create a DataFrame matching the EXACT column structure used in Jupyter
#         input_data = pd.DataFrame(
#             [[car_model, company, year, kms_driven, fuel_type]],
#             columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
#         )
#
#         # 4. Make prediction and extract the float value
#         prediction = model.predict(input_data)
#
#         # 5. Round the prediction to 2 decimal places and return it as a string
#         return str(np.round(prediction[0], 2))
#
#     except Exception as e:
#         # If anything breaks, it will print the exact issue in the PyCharm terminal
#         print(f"ERROR DURING PREDICTION: {e}")
#         return "Error calculation failed on server backend."
@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # 1. Get data from the form matching the new HTML names
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')

    # CRITICAL FIX: Make sure this is 'kilo_driven' to match index.html
    kms_driven = int(request.form.get('kilo_driven'))

    # 2. Predict using the exact column structure from your training data
    prediction = model.predict(pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    ))

    # 3. Return the clean number
    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)