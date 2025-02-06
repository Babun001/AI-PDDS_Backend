# created on 26/07/2024 by babun

from flask import Flask, request, jsonify
import pickle



app = Flask(__name__)

### load models 
def load_Models(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)
    

models = {
    "diabetes_model" : load_Models("./Models/Diabetes.pkl"),
    "liver_model" : load_Models("./Models/Liver_rf_babun.pkl"),
    "kidney_model" : load_Models("./Models/ckd-rf-scaled.pkl"),
    "parkinsons_model" : load_Models("./Models/parkinsons-rf-refresh.pkl"),
    "breast_model" : load_Models("./Models/breastCancer-rf-recheck.pkl"),
    "heart_model" : load_Models("./Models/heart-gbc-updated.pkl"),
    "lung_model" : load_Models("./Models/lungCancer-lr.pkl"),
    "stroke_model" : load_Models("./Models/stroke-rf.pkl")
}


# pickle_in_diabetes = open("./Models/Diabetes.pkl","rb")
# model = pickle.load(pickle_in_diabetes)

# pickle_in_liver = open("./Models/Liver_rf_babun.pkl","rb")
# liver_model = pickle.load(pickle_in_liver)

# pickle_in_kidney = open("./Models/ckd-rf-scaled.pkl", "rb")
# kidney_model = pickle.load(pickle_in_kidney)

# pickle_in_parkinson = open("./Models/parkinsons-rf-refresh.pkl", "rb")
# parkinsons_model = pickle.load(pickle_in_parkinson)

# pickle_in_breast = open("./Models/breastCancer-rf-recheck.pkl", "rb")
# breast_model = pickle.load(pickle_in_breast)

# pickle_in_heart = open("./Models/heart-gbc-updated.pkl", "rb")
# heart_model = pickle.load(pickle_in_heart)

# pickle_in_lung = open("./Models/lungCancer-lr.pkl", "rb")
# lung_model = pickle.load(pickle_in_lung)


### diabetes module
from DiseaseModules.diabetes import Diabetes_prediction
@app.route('/diabetes', methods=["post"])
def diabetes():
    return Diabetes_prediction(models["diabetes_model"])



### liver module
from DiseaseModules.liver_prediction import liver_prediction
@app.route('/liver', methods=["post"])
def liver():
    return liver_prediction(models["liver_model"])
    
    


### kidney module
from DiseaseModules.kidney import kidney_prediction
@app.route('/kidney', methods=["post"])
def kidney():
    return kidney_prediction(models["kidney_model"])




### parkinson module  
from DiseaseModules.parkinson import Parkinson_Prediction
@app.route('/parkinson',methods=["post"])
def parkinson():
    return Parkinson_Prediction(models["parkinsons_model"])



### breast module
from DiseaseModules.breast import breast_Prediction
@app.route('/breast', methods=["post"])
def breast():
    return breast_Prediction(models["breast_model"])


###  heart module
from DiseaseModules.heart import heart_prediction
@app.route("/heart", methods=["post"])
def heart():
    return heart_prediction(models["heart_model"])



### lung module
from DiseaseModules.lung import lung_prediction
@app.route("/lung", methods=["post"])
def lung():
    return lung_prediction(models["lung_model"])



### stroke model
from DiseaseModules.stroke import stroke_prediction
@app.route("/stroke", methods=["post"])
def stroke():
    return stroke_prediction(models["stroke_model"])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
# the api is http://127.0.0.1:5000/*