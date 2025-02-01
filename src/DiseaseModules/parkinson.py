from flask import request, jsonify

def Parkinson_Prediction(parkinsons_model):
    try:
        data = request.get_json()
        if not data :
            return jsonify({
                "error":"unable to fetch paitent data forn parkinson",
                "status":"failed"
            }),402
                
        print(data)
            
        mdvp_fo_hz = data.get("mdvp_fo_hz")
        mdvp_fhi_hz = data.get("mdvp_fhi_hz")
        mdvp_flo_hz = data.get("mdvp_flo_hz")
        mdvp_jitter_in_percent = data.get("mdvp_jitter_in_percent")
        mdvp_jitter_abs = data.get("mdvp_jitter_abs")
        mdvp_rap = data.get("mdvp_rap")
        mdvp_ppq = data.get("mdvp_ppq")
        jitter_ddp = data.get("jitter_ddp")
        mdvp_shimmer = data.get("mdvp_shimmer")
        mdvp_shimmer_db = data.get("mdvp_shimmer_db")
        shimmer_apq3 = data.get("shimmer_apq3")
        shimmer_apq5 = data.get("shimmer_apq5")
        mdvp_apq = data.get("mdvp_apq")
        shimmer_dda = data.get("shimmer_dda")
        nhr = data.get("nhr")
        hnr = data.get("hnr")
        rpde = data.get("rpde")
        dfa = data.get("dfa")
        spread1 = data.get("spread1")
        spread2 = data.get("spread2")
        d2 = data.get("d2")
        ppe = data.get("ppe")
        
        
        print(
            mdvp_fo_hz,
            mdvp_fhi_hz,
            mdvp_flo_hz,
            mdvp_jitter_in_percent,
            mdvp_jitter_abs,
            mdvp_rap,
            mdvp_ppq,
            jitter_ddp,
            mdvp_shimmer,
            mdvp_shimmer_db,
            shimmer_apq3,
            shimmer_apq5,
            mdvp_apq,
            shimmer_dda,
            nhr,
            hnr,
            rpde,
            dfa,
            spread1,
            spread2,
            d2,
            ppe
        )
        
        parkinsonsPrediction = parkinsons_model.predict([[
        
            float(mdvp_fo_hz),
            float(mdvp_fhi_hz),
            float(mdvp_flo_hz),
            float(mdvp_jitter_in_percent),
            float(mdvp_jitter_abs),
            float(mdvp_rap),
            float(mdvp_ppq),
            float(jitter_ddp),
            float(mdvp_shimmer),
            float(mdvp_shimmer_db),
            float(shimmer_apq3),
            float(shimmer_apq5),
            float(mdvp_apq),
            float(shimmer_dda),
            float(nhr),
            float(hnr),
            float(rpde),
            float(dfa),
            float(spread1),
            float(spread2),
            float(d2),
            float(ppe)
        
        ]])
        
        print("Predicted value: ",parkinsonsPrediction)
        
        if not parkinsonsPrediction:
            return jsonify({
                "error":"Unable to predict parkinsons disease!",
                "status":"failed"
            }),400
        return jsonify({"paitentData":str(parkinsonsPrediction)}),200
            
    except Exception as e:
        return jsonify({
            "Error": "error in parkinson disease module",
            'status':"failed",
            "err":str(e)
        }),400