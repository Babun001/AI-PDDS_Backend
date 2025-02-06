from flask import request, jsonify

def heart_prediction(heart_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error":"unable to get data from kidney api",
                "status" : "failed"
            }),404
        
        Age  = data.get("Age")
        Sex  = data.get("Sex")
        ChestPainType  = data.get("ChestPainType")
        RestingBP  = data.get("RestingBP")
        Cholesterol  = data.get("Cholesterol")
        FastingBS  = data.get("FastingBS")
        RestingECG  = data.get("RestingECG")
        MaxHR  = data.get("MaxHR")
        ExerciseAngina  = data.get("ExerciseAngina")
        Oldpeak  = data.get("Oldpeak")
        ST_Slope  = data.get("ST_Slope")
        # HeartDisease= data.get("HeartDisease")
        
        # print(
        #     Age,       
        #     Sex,
        #     ChestPainType,
        #     RestingBP,
        #     Cholesterol,
        #     FastingBS,
        #     RestingECG,
        #     MaxHR,
        #     ExerciseAngina,
        #     Oldpeak,
        #     ST_Slope,
        #     # HeartDisease)
        # )
        
        heart_predicted_value = heart_model.predict([[
            
            float(Age),
            float(Sex),
            float(ChestPainType),
            float(RestingBP),
            float(Cholesterol),
            float(FastingBS),
            float(RestingECG),
            float(MaxHR),
            float(ExerciseAngina),
            float(Oldpeak),
            float(ST_Slope)
            
        ]])
        if not heart_predicted_value:
            return jsonify({"error":"Unable to predict heart disease","status":"failed"}),404
        
        return jsonify({
            "patientData": str(heart_predicted_value)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})
    
    
    
    
    
