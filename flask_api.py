# created on 26/07/2024 by babun

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle



app = Flask(__name__)
pickle_in = open("./AIPDDS_Backend/Models/Diabetes.pkl","rb")
model = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return ("Welcome all!")


@app.route('/diabetes', methods=['GET'])
def Diabetes_prediction():
    Pregnancies = request.args.get('Pregnancies')
    Glucose = request.args.get('Glucose')
    BloodPressure = request.args.get('BloodPressure')
    Insulin = request.args.get('Insulin')
    BMI = request.args.get('BMI')
    DiabetesPedigreeFunction = request.args.get('DiabetesPedigreeFunction')
    Age = request.args.get('Age')
    predicted_value = model.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    return predicted_value



if __name__ == '__main__':
    app.run()