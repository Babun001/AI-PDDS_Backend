from flask import request, jsonify
import numpy as np
import cv2
import requests
from constants.preprocessImage import preprocess_image

def tuberculosis_prediction(tuberculosis_model):
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error" : "Data not received!!"
            })
        img_url = data.get("cloudinaryImageLink")
        
        response = requests.get(img_url)

        if response.status_code != 200:
            return jsonify({
                "error": "Failed to download image",
                "status": "400"
            }), 400
            
        image = np.array(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        processed_image = preprocess_image(image)
        
        image = cv2.imread(processed_image, cv2.IMREAD_GRAYSCALE)

        # Resize to match model input size
        image = cv2.resize(image, (224, 224))

        # Expand dimensions to match model input shape (batch_size, height, width, channels)
        image = np.expand_dims(image, axis=-1)  # Add channel dimension
        image = np.expand_dims(image, axis=0)   # Add batch dimension

        # Normalize if required
        image = image.astype("float32") / 255.0
        
        prediction = tuberculosis_model.predict(image)
        print(prediction)
        # predicted_class = np.argmax(prediction)
        # confidence = float(np.max(prediction))
        
        # disease_stage = tuberculosis_model.get(predicted_class, "Unknown")

        return jsonify({
            "predicted_stage": str(0),
            "confidence": str(100)
        })
        
    except Exception as e:
        return jsonify({
            "error":str(e),
            "status" : "failed"
        })
