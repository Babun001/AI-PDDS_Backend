from flask import request, jsonify

def kidney_prediction(kidney_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error":"unable to get data from kidney api",
                "status" : "failed"
            }),404
        age = data.get('age')                     
        blood_pressure = data.get('blood_pressure')          
        specific_gravity = data.get('specific_gravity')        
        albumin = data.get('albumin')                 
        sugar = data.get('sugar')                   
        blood_glucose_random = data.get('blood_glucose_random')    
        blood_urea = data.get('blood_urea')              
        serum_creatinine = data.get('serum_creatinine')        
        sodium = data.get('sodium')                  
        potassium = data.get('potassium')               
        haemoglobin = data.get('haemoglobin')             
        packed_cell_volume = data.get('packed_cell_volume')      
        white_blood_cell_count = data.get('white_blood_cell_count')  
        red_blood_cell_count = data.get('red_blood_cell_count')  

        kidney_predicted_value =   kidney_model.predict([[
            float(age),float(blood_pressure),
            float(specific_gravity),
            float(albumin),
            float(sugar),
            float(blood_glucose_random),
            float(blood_urea),
            float(serum_creatinine),
            float(sodium),
            float(potassium),
            float(haemoglobin),
            float(packed_cell_volume),
            float(white_blood_cell_count),
            float(red_blood_cell_count)
        ]])
        
        return jsonify({
            "patientData": str(kidney_predicted_value)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})