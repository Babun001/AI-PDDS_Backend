from flask import request, jsonify

def Diabetes_prediction(model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error": "No such json file found!", "status" : "failed"
            })
        
        Pregnancies = data.get('Pregnancies')
        Glucose = data.get('Glucose')
        BloodPressure = data.get('BloodPressure')
        Insulin = data.get('Insulin')
        BMI = data.get('BMI')
        DiabetesPedigreeFunction = data.get('DiabetesPedigreeFunction')
        Age = data.get('Age')
        # print("-------------------------------------------------------------------------------------------")
        # print([Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age])
        predicted_value = model.predict([[float(Pregnancies),float(Glucose),float(BloodPressure),float(Insulin),float(BMI),float(DiabetesPedigreeFunction),float(Age)]])
        # print(predicted_value)
        
        return jsonify({'patientData': str(predicted_value)})
    
    except Exception  as e:
        return jsonify({"error": str(e), "status": "failed"})