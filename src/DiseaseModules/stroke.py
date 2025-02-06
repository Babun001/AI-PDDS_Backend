from flask import request, jsonify

def stroke_prediction(strokeModel):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error":"unable to get data from lung api",
                "status" : "failed"
            }),404
            
        print(data)
        
        age = float(data.get("age"))
        hypertension = float(data.get("hypertension"))
        heart_disease = float(data.get("heart_disease"))
        ever_married = float(data.get("ever_married"))
        avg_glucose_level = float(data.get("avg_glucose_level"))
        bmi = float(data.get("bmi"))
        
        print(age,
            hypertension,
            heart_disease,
            ever_married,
            avg_glucose_level,
            bmi)
        
        stroke_predictedData = strokeModel.predict([[
            age,
            hypertension,
            heart_disease,
            ever_married,
            avg_glucose_level,
            bmi
        ]])
        
        
        
        # if not stroke_predictedData:
        #     return jsonify({
        #         "error":"unable to predict stroke disease",
        #         "status" : "failed"
        #     }),400
            
        print(str(stroke_predictedData))    
        
        return jsonify({
            "patientData": str(stroke_predictedData)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})
    
    
    
    
   