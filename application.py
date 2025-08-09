import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

try:
    ridge_model = pickle.load(open('model/model.pkl', 'rb'))
    standard_scaler = pickle.load(open('model/scaler.pkl', 'rb'))
except FileNotFoundError:
    print("Error: The model or scaler files were not found. Please ensure 'model/model.pkl' and 'model/scaler.pkl' exist.")

feature_list = [
    'male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
    'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol',
    'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            user_data = [
                float(request.form.get('male')),
                float(request.form.get('age')),
                float(request.form.get('currentSmoker')),
                float(request.form.get('cigsPerDay')),
                float(request.form.get('BPMeds')),
                float(request.form.get('prevalentStroke')),
                float(request.form.get('prevalentHyp')),
                float(request.form.get('diabetes')),
                float(request.form.get('totChol')),
                float(request.form.get('sysBP')),
                float(request.form.get('diaBP')),
                float(request.form.get('BMI')),
                float(request.form.get('heartRate')),
                float(request.form.get('glucose'))
            ]
        except (ValueError, TypeError) as e:
            print(f"Error processing form data: {e}")
            return render_template('home.html', error_message="Invalid input data. Please check your entries.")

        new_data_array = np.array(user_data).reshape(1, -1)
        new_data_scaled = standard_scaler.transform(new_data_array)
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)