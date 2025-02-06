from flask import request, jsonify

def liver_prediction(liver_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": 'liver api failed to get data!!', "status":"dailed"}),404
        
        Age  = data.get('Age')
        Gender = data.get('Gender')
        Total_Bilirubin = data.get('Total_Bilirubin')
        Alamine_Aminotransferase = data.get('Alamine_Aminotransferase')
        Aspartate_Aminotransferase = data.get('Aspartate_Aminotransferase')
        Total_Proteins = data.get('Total_Proteins')
        Albumin = data.get('Albumin')
        Albumin_and_Globulin_Ratio  = data.get('Albumin_and_Globulin_Ratio')
        
        # print(Age,Gender,Total_Bilirubin,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Proteins,Albumin,Albumin_and_Globulin_Ratio)
    
        liver_predicted_value = liver_model.predict([[
            float(Age) ,
            float(Gender),
            float(Total_Bilirubin),
            float(Alamine_Aminotransferase),
            float(Aspartate_Aminotransferase),
            float(Total_Proteins),
            float(Albumin),
            float(Albumin_and_Globulin_Ratio)        
            ]])
        
        # print(liver_predicted_value)
        return jsonify({"patientData":str(liver_predicted_value)})
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})
    