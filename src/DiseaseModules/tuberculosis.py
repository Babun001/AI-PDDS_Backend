from flask import request, jsonify
import numpy as np
import cv2
from constants.preprocessImage import preprocess_image

def tuberculosis_prediction():
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error" : "Data not received!!"
            })
        img_path = data.get("")
        
    except Exception as e:
        return jsonify({
            "error":str(e),
            "status" : "failed"
        })
