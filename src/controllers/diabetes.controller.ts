import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import axios from "axios";
import apiError from "../utility/apiError";

const diabetesController = asyncAwaitFunc(async (req, res) => {
    try {
        const { Pregnancies,
            Glucose,
            BloodPressure,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age } = req.body;


        const response = await axios.post('http://127.0.0.1:5000/diabetes', {
            Pregnancies,
            Glucose,
            BloodPressure,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        },
            {
                headers: { "Content-Type": "application/json" }
            })

        if(!response){
            throw new apiError(404,"result not received","");
        }
        res.status(200).json({
            message:"Received Paitent data",
            data:response.data
        })
        

    } catch (error: any) {
        console.error("Error in diabetesController:", error);
        throw new apiError(404, "Bad request in diabetesController", error.message || "");
    }
})


export default diabetesController;