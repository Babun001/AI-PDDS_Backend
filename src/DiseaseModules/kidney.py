from flask import request, jsonify

def kidney_prediction(kidney_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error":"unable to get data from kidney api",
                "status" : "failed"
            }),404
          
        
        age = data.get("age")
        blood_pressure = data.get("blood_pressure")
        specific_gravity = data.get("specific_gravity")
        albumin = data.get("albumin")
        sugar = data.get("sugar")
        red_blood_cells = data.get("red_blood_cells")
        pus_cell = data.get("pus_cell")
        pus_cell_clumps = data.get("pus_cell_clumps")
        bacteria = data.get("bacteria")
        blood_glucose_random = data.get("blood_glucose_random")
        blood_urea = data.get("blood_urea")
        serum_creatinine = data.get("serum_creatinine")
        sodium = data.get("sodium")
        potassium = data.get("potassium")
        haemoglobin = data.get("haemoglobin")
        packed_cell_volume = data.get("packed_cell_volume")
        white_blood_cell_count = data.get("white_blood_cell_count")
        red_blood_cell_count = data.get("red_blood_cell_count")
        hypertension = data.get("hypertension")
        diabetes_mellitus = data.get("diabetes_mellitus")
        coronary_artery_disease = data.get("coronary_artery_disease")
        appetite = data.get("appetite")
        peda_edema = data.get("peda_edema")
        aanemia = data.get("aanemia")
        
        print(
age,
blood_pressure,
specific_gravity,
albumin,
sugar,
red_blood_cells,
pus_cell,
pus_cell_clumps,
bacteria,
blood_glucose_random,
blood_urea,
serum_creatinine,
sodium,
potassium,
haemoglobin,
packed_cell_volume,
white_blood_cell_count,
red_blood_cell_count,
hypertension,
diabetes_mellitus,
coronary_artery_disease,
appetite,
peda_edema,
aanemia
)

        kidney_predicted_value =   kidney_model.predict([[
        float(age),
        float(blood_pressure),
        float(specific_gravity),
        float(albumin),
        float(sugar),
        float(red_blood_cells),
        float(pus_cell),
        float(pus_cell_clumps),
        float(bacteria),
        float(blood_glucose_random),
        float(blood_urea),
        float(serum_creatinine),
        float(sodium),
        float(potassium),
        float(haemoglobin),
        float(packed_cell_volume),
        float(white_blood_cell_count),
        float(red_blood_cell_count),
        float(hypertension),
        float(diabetes_mellitus),
        float(coronary_artery_disease),
        float(appetite),
        float(peda_edema),
        float(aanemia)
        ]])
        
        return jsonify({
            "patientData": str(kidney_predicted_value)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})