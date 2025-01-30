from flask import request,jsonify

def lung_prediction(lung_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error":"unable to get data from lung api",
                "status" : "failed"
            }),404
        
        
        Age = data.get("Age"),
        Gender = data.get("Gender"),
        Air_Pollution = data.get("Air_Pollution"),
        Alcohol_use = data.get("Alcohol_use"),
        Dust_Allergy = data.get("Dust_Allergy"),
        OccuPational_Hazards = data.get("OccuPational_Hazards"),
        Genetic_Risk = data.get("Genetic_Risk"),
        chronic_Lung_Disease = data.get("chronic_Lung_Disease"),
        Balanced_Diet = data.get("Balanced_Diet"),
        Obesity = data.get("Obesity"),
        Smoking = data.get("Smoking"),
        Passive_Smoker = data.get("Passive_Smoker"),
        Chest_Pain = data.get("Chest_Pain"),
        Coughing_of_Blood = data.get("Coughing_of_Blood"),
        Fatigue = data.get("Fatigue"),
        Weight_Loss = data.get("Weight_Loss"),
        Shortness_of_Breath = data.get("Shortness_of_Breath"),
        Wheezing = data.get("Wheezing"),
        Swallowing_Difficulty = data.get("Swallowing_Difficulty"),
        Clubbing_of_Finger_Nails = data.get("Clubbing_of_Finger_Nails"),
        Frequent_Cold = data.get("Frequent_Cold"),
        Dry_Cough = data.get("Dry_Cough"),
        Snoring = data.get("Snoring")
        
        print(
            Age,
            Gender,
            Air_Pollution,
            Alcohol_use,
            Dust_Allergy,
            OccuPational_Hazards,
            Genetic_Risk,
            chronic_Lung_Disease,
            Balanced_Diet,
            Obesity,
            Smoking,
            Passive_Smoker,
            Chest_Pain,
            Coughing_of_Blood,
            Fatigue,
            Weight_Loss,
            Shortness_of_Breath,
            Wheezing,
            Swallowing_Difficulty,
            Clubbing_of_Finger_Nails,
            Frequent_Cold,
            Dry_Cough,
            Snoring)


        lung_predicted_value =   lung_model.predict([[
            float(Age),
            float(Gender),
            float(Air_Pollution),
            float(Alcohol_use),
            float(Dust_Allergy),
            float(OccuPational_Hazards),
            float(Genetic_Risk),
            float(chronic_Lung_Disease),
            float(Balanced_Diet),
            float(Obesity),
            float(Smoking),
            float(Passive_Smoker),
            float(Chest_Pain),
            float(Coughing_of_Blood),
            float(Fatigue),
            float(Weight_Loss),
            float(Shortness_of_Breath),
            float(Wheezing),
            float(Swallowing_Difficulty),
            float(Clubbing_of_Finger_Nails),
            float(Frequent_Cold),
            float(Dry_Cough),
            float(Snoring)
        ]])
        
        if not lung_predicted_value:
            return jsonify({"error":"Unable to predict lung disease!!","status":"failed"}),404
        
        return jsonify({
            "patientData": str(lung_predicted_value)
        })
        
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"})
    