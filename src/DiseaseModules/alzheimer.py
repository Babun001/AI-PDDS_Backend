from flask import request, jsonify
import requests
import numpy as np
import cv2
import tensorflow as tf
from constants.preprocessImage import preprocess_image


def alzheimer_prediction(alzheimer_model):
    try:
        
        data = request.get_json()
        img_url = data.get("imgLink")
        if not img_url :
            return jsonify({
                "error":"img url not received! at alzheimer end",
                "status":"400"
            })


        ### download the image from url
        response = requests.get(img_url)

        if response.status_code != 200:
            return jsonify({
                "error": "Failed to download image",
                "status": "400"
            }), 400


        image = np.array(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        processed_image = preprocess_image(image)
        
        

        prediction = alzheimer_model.predict(processed_image)
        predicted_class = np.argmax(prediction)
        confidence = float(np.max(prediction))
        
        alzheimer_classes = {
            0: "Mild Dementia",
            1: "Moderate Dementia",
            2: "Non-Demented",
            3: "Very Mild Dementia"
        }
        disease_stage = alzheimer_classes.get(predicted_class, "Unknown")

        return jsonify({
            "predicted_stage": disease_stage,
            "confidence": confidence
        })
        
    except Exception as e:
        return jsonify({
            "Error": str(e),
            "Status" : "400"
        })
     


