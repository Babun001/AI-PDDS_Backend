import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const stroke_controller = asyncAwaitFunc(async(req, res) =>{
    try {

        const {
            age,
            hypertension,
            heart_disease,
            ever_married,
            avg_glucose_level,
            bmi
        } = req.body;

        // console.table([age,
        //     hypertension,
        //     heart_disease,
        //     ever_married,
        //     avg_glucose_level,
        //     bmi])

        const response = await axios.post("http://127.0.0.1:5000/stroke",
            {
                age,
                hypertension,
                heart_disease,
                ever_married,
                avg_glucose_level,
                bmi
            },
            {
                headers: { "Content-Type": "application/json" }
            }
        )


        res.status(200).json({
            patientData: response.data
        })


    } catch (error) {
        throw new apiError(404, "stroke controller is not working...!!", "")
    }
})

export default stroke_controller;