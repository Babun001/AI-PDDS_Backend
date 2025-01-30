from flask import request, jsonify

def breast_Prediction(breast_model):
    try:
        data = request.get_json()
        if not data :
            return jsonify({
                "Error":"Patient data not received for breast prediction !!",
                "status":"failed"
            }),404
            
        diagnosis = data.get("diagnosis"),
        radius_mean = data.get("radius_mean"),
        texture_mean = data.get("texture_mean"),
        perimeter_mean = data.get("perimeter_mean"),
        area_mean = data.get("area_mean"),
        smoothness_mean = data.get("smoothness_mean"),
        compactness_mean = data.get("compactness_mean"),
        concavity_mean = data.get("concavity_mean"),
        concave_points_mean = data.get("concave points_mean"),
        symmetry_mean = data.get("symmetry_mean"),
        fractal_dimension_mean = data.get("fractal_dimension_mean"),
        radius_se = data.get("radius_se"),
        texture_se = data.get("texture_se"),
        perimeter_se = data.get("perimeter_se"),
        area_se = data.get("area_se"),
        smoothness_se = data.get("smoothness_se"),
        compactness_se = data.get("compactness_se"),
        concavity_se = data.get("concavity_se"),
        concave_points_se = data.get("concave points_se"),
        symmetry_se = data.get("symmetry_se"),
        fractal_dimension_se = data.get("fractal_dimension_se"),
        radius_worst = data.get("radius_worst"),
        texture_worst  = data.get("texture_worst"),
        perimeter_worst = data.get("perimeter_worst"),
        area_worst = data.get("area_worst"),
        smoothness_worst = data.get("smoothness_worst"),
        compactness_worst = data.get("compactness_worst"),
        concavity_worst = data.get("concavity_worst"),
        concave_points_worst = data.get("concave points_worst"),
        symmetry_worst = data.get("symmetry_worst"),
        fractal_dimension_worst = data.get("fractal_dimension_worst")
        
        print(diagnosis,
            radius_mean,
            texture_mean,
            perimeter_mean,
            area_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            concave_points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            radius_se,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            concave_points_se,
            symmetry_se,
            fractal_dimension_se,
            radius_worst,
            texture_worst,
            perimeter_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            concave_points_worst,
            symmetry_worst,
            fractal_dimension_worst)
        
        breast_predicted_value = breast_model.predict([[
            float(diagnosis),
            float(radius_mean),
            float(texture_mean),
            float(perimeter_mean),
            float(area_mean),
            float(smoothness_mean),
            float(compactness_mean),
            float(concavity_mean),
            float(concave_points_mean),
            float(symmetry_mean),
            float(fractal_dimension_mean),
            float(radius_se),
            float(texture_se),
            float(perimeter_se),
            float(area_se),
            float(smoothness_se),
            float(compactness_se),
            float(concavity_se),
            float(concave_points_se),
            float(symmetry_se),
            float(fractal_dimension_se),
            float(radius_worst),
            float(texture_worst),
            float(perimeter_worst),
            float(area_worst),
            float(smoothness_worst),
            float(compactness_worst),
            float(concavity_worst),
            float(concave_points_worst),
            float(symmetry_worst),
            float(fractal_dimension_worst)
        ]])
        
        if not breast_predicted_value:
            return jsonify({"error":"unable to predict breast disease!!!", "status":"failed"}),404
        
        return jsonify({
            "patientData": str(breast_predicted_value)
        })
            
    except Exception as e:
        return jsonify({
            "Error":"Error in breast_Prediction method",
            "status":"failed"
        }),404