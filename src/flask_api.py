# created on 26/07/2024 by babun

from flask import Flask, request, jsonify
import pickle



app = Flask(__name__)

pickle_in_diabetes = open("./Models/Diabetes.pkl","rb")
model = pickle.load(pickle_in_diabetes)

pickle_in_liver = open("./Models/Liver_rf_babun.pkl","rb")
liver_model = pickle.load(pickle_in_liver)

pickle_in_kidney = open("./Models/ckd-rf-scaled.pkl", "rb")
kidney_model = pickle.load(pickle_in_kidney)

pickle_in_parkinson = open("./Models/parkinsons-rf.pkl", "rb")
parkinsons_model = pickle.load(pickle_in_parkinson)

pickle_in_breast = open("./Models/breastCancer-rf.pkl", "rb")
breast_model = pickle.load(pickle_in_breast)

pickle_in_heart = open("./Models/heartDisease-gbc.pkl", "rb")
heart_model = pickle.load(pickle_in_heart)

pickle_in_lung = open("./Models/lungCancer-lr.pkl", "rb")
lung_model = pickle.load(pickle_in_lung)



@app.route('/diabetes')
def Diabetes_prediction():
    print("api called")
    try:
        Pregnancies = request.args.get('Pregnancies')
        Glucose = request.args.get('Glucose')
        BloodPressure = request.args.get('BloodPressure')
        Insulin = request.args.get('Insulin')
        BMI = request.args.get('BMI')
        DiabetesPedigreeFunction = request.args.get('DiabetesPedigreeFunction')
        Age = request.args.get('Age')
        predicted_value = model.predict([[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        return jsonify({'patientData': str(predicted_value)})
    except Exception  as e:
        return jsonify({"error": str(e), "status": "failed"})

@app.route('/liver')
def liver_prediction():
    try:
        Age  = request.args.get('Age')
        Gender = request.args.get('Gender')
        Total_Bilirubin = request.args.get('Total_Bilirubin')
        Alamine_Aminotransferase = request.args.get('Alamine_Aminotransferase')
        Aspartate_Aminotransferase = request.args.get('Aspartate_Aminotransferase')
        Total_Proteins = request.args.get('Total_Proteins')
        Albumin = request.args.get('Albumin')
        Albumin_and_Globulin_Ratio  = request.args.get('Albumin_and_Globulin_Ratio')
    
        liver_predicted_value = liver_model.predict([[
            Age ,
            Gender,
            Total_Bilirubin,
            Alamine_Aminotransferase,
            Aspartate_Aminotransferase,
            Total_Proteins,
            Albumin,
            Albumin_and_Globulin_Ratio        
            ]])
        return jsonify({"patientData":str(liver_predicted_value)})

    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})

@app    .route('/kidney')
def kidney_prediction():
    try:
        age = request.args.get('age')                     
        blood_pressure = request.args.get('blood_pressure')          
        specific_gravity = request.args.get('specific_gravity')        
        albumin = request.args.get('albumin')                 
        sugar = request.args.get('sugar')                   
        blood_glucose_random = request.args.get('blood_glucose_random')    
        blood_urea = request.args.get('blood_urea')              
        serum_creatinine = request.args.get('serum_creatinine')        
        sodium = request.args.get('sodium')                  
        potassium = request.args.get('potassium')               
        haemoglobin = request.args.get('haemoglobin')             
        packed_cell_volume = request.args.get('packed_cell_volume')      
        white_blood_cell_count = request.args.get('white_blood_cell_count')  
        red_blood_cell_count = request.args.get('red_blood_cell_count')  

        kidney_predicted_value =   kidney_model.predict([[
            age,
            blood_pressure,
            specific_gravity,
            albumin,
            sugar,
            blood_glucose_random,
            blood_urea,
            serum_creatinine,
            sodium,
            potassium,
            haemoglobin,
            packed_cell_volume,
            white_blood_cell_count,
            red_blood_cell_count
        ]])
        
        return jsonify({
            "patientData": str(kidney_predicted_value)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})
    


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
# the api is http://127.0.0.1:5000/*