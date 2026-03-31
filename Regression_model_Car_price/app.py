from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
 
app = Flask(__name__)
CORS(app)
 
pip = pickle.load(open('car_model.pkl', 'rb'))
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
 
    input_df = pd.DataFrame([{
        'Make':                data['make'],
        'Fuel Type':           data['fuel_type'],
        'Drivetrain':          data['drivetrain'],
        'Transmission':        data['transmission'],
        'Kilometer':           int(data['kilometer']),
        'Engine':              float(data['engine']),
        'Length':              float(data['length']),
        'Width':               float(data['width']),
        'Height':              float(data['height']),
        'Fuel Tank Capacity':  float(data['fuel_tank_capacity']),
        'Max Power bhp':       float(data['max_power_bhp']),
        'Max Power rpm':       float(data['max_power_rpm']),
        'Max Torque Nm':       float(data['max_torque_nm']),
        'Max Torque Rpm':      float(data['max_torque_rpm']),
        'Car_age':             int(data['car_age']),
    }])
 
    log_prediction = pip.predict(input_df)[0]
    actual_price = np.expm1(log_prediction)
    return jsonify({'predicted_price': round(float(actual_price), 2)})
 
if __name__ == '__main__':
    app.run(debug=True,port=5000)