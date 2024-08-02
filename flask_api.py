# created on 26/07/2024 by babun

from flask import Flask, request
import pickle



app = Flask(__name__)
pickle_in_diabetes = open("./AIPDDS_Backend/Models/Diabetes.pkl","rb")
model = pickle.load(pickle_in_diabetes)

pickle_in_liver = open("./AIPDDS_Backend/Models/Liver_rf_babun.pkl","rb")
liver_model = pickle.load(pickle_in_liver)


@app.route('/diabetes')
def Diabetes_prediction():
    Pregnancies = request.args.get('Pregnancies')
    Glucose = request.args.get('Glucose')
    BloodPressure = request.args.get('BloodPressure')
    Insulin = request.args.get('Insulin')
    BMI = request.args.get('BMI')
    DiabetesPedigreeFunction = request.args.get('DiabetesPedigreeFunction')
    Age = request.args.get('Age')
    predicted_value = model.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    return str(predicted_value)


@app.route('/liver')
def liver_prediction():
    Age  = request.args.get('Age')
    Gender = request.args.get('Gender')
    Total_Bilirubin = request.args.get('Total_Bilirubin')
    Alamine_Aminotransferase = request.args.get('Alamine_Aminotransferase')
    Aspartate_Aminotransferase = request.args.get('Aspartate_Aminotransferase')
    Total_Protines = request.args.get('Total_Protines')
    Albumin = request.args.get('Albumin')
    Albumin_and_Globulin_Ratio  = request.args.get('Albumin_and_Globulin_Ratio')
    
    liver_predicted_value = liver_model.predict([[
        Age ,
        Gender,
        Total_Bilirubin,
        Alamine_Aminotransferase,
        Aspartate_Aminotransferase,
        Total_Protines,
        Albumin,
        Albumin_and_Globulin_Ratio        
    ]])
    return str(liver_predicted_value)


if __name__ == '__main__':
    app.run()