import cv2
import numpy as np

def preprocess_image(image):
    ###Preprocess the image for the ML model
    # Adjust size based on model input shape
    image = cv2.resize(image, (224, 224)) 
    # Normalize 
    image = image / 255.0  
    # Add batch dimension
    image = np.expand_dims(image, axis=0)  
    return image