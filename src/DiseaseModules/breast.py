from flask import request, jsonify

def breast_Prediction(breast_model):
    try:
        data = request.get_json()
        if not data :
            return jsonify({
                "Error":"Patient data not received for breast prediction !!",
                "status":"failed"
            }),404
            
        print(data)
            
        radius_mean = float(data.get("radius_mean"))
        texture_mean = float(data.get("texture_mean"))
        perimeter_mean = float(data.get("perimeter_mean"))
        area_mean = float(data.get("area_mean"))
        smoothness_mean = float(data.get("smoothness_mean"))
        compactness_mean = float(data.get("compactness_mean"))
        concavity_mean = float(data.get("concavity_mean"))
        concave_points_mean = float(data.get("concave_points_mean"))
        symmetry_mean = float(data.get("symmetry_mean"))
        fractal_dimension_mean = float(data.get("fractal_dimension_mean"))
        radius_se = float(data.get("radius_se"))
        texture_se = float(data.get("texture_se"))
        perimeter_se = float(data.get("perimeter_se"))
        area_se = float(data.get("area_se"))
        smoothness_se = float(data.get("smoothness_se"))
        compactness_se = float(data.get("compactness_se"))
        concavity_se = float(data.get("concavity_se"))
        concave_points_se = float(data.get("concave_points_se"))
        symmetry_se = float(data.get("symmetry_se"))
        fractal_dimension_se = float(data.get("fractal_dimension_se"))
        radius_worst = float(data.get("radius_worst"))
        texture_worst = float(data.get("texture_worst"))
        perimeter_worst = float(data.get("perimeter_worst"))
        area_worst = float(data.get("area_worst"))
        smoothness_worst = float(data.get("smoothness_worst"))
        compactness_worst = float(data.get("compactness_worst"))
        concavity_worst = float(data.get("concavity_worst"))
        concave_points_worst = float(data.get("concave_points_worst"))
        symmetry_worst = float(data.get("symmetry_worst"))
        fractal_dimension_worst = float(data.get("fractal_dimension_worst"))
        
        print(
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
            fractal_dimension_worst
        )
        
        breast_predicted_value = breast_model.predict([[
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
            fractal_dimension_worst
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
        
