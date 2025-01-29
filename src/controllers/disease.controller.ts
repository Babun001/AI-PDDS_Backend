import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const checkServer = asyncAwaitFunc((req, res) => {
    try {
        res.status(201).json({
            message: "all okay"
        })
    } catch (error) {

    }
})

const diabetesController = asyncAwaitFunc(async (req, res) => {
    try {
        const { Pregnancies,
            Glucose,
            BloodPressure,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age } = req.body;

        // console.table({ Pregnancies,
        //     Glucose,
        //     BloodPressure,
        //     Insulin,
        //     BMI,
        //     DiabetesPedigreeFunction,
        //     Age });


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

const liverController = asyncAwaitFunc((req, res) => {
    try {
        const queryParams = req.query;
        // console.log(queryParams);

        res.status(200).json(queryParams)

    } catch (error) {
        throw new apiError(404, "bad request in liverController", "")
    }
})

const kidneyController = asyncAwaitFunc((req, res) => {
    try {
        res.status(202).json({
            mess: "kidneyController"
        })
    } catch (error) {
        throw new apiError(404, "bad request in kidneyController", "")
    }
})

const parkinsonController = asyncAwaitFunc((req, res) => {
    try {
        const queryParams = req.query;
        // console.log(queryParams);

        res.status(200).json(queryParams)
    } catch (error) {
        throw new apiError(404, "bad request in parkinsonController", "")
    }
})

const breastController = asyncAwaitFunc((req, res) => {
    try {
        const queryParams = req.query;
        // console.log(queryParams);

        res.status(200).json(queryParams)
    } catch (error) {
        throw new apiError(404, "bad request in breastController", "")
    }
})

export {
    checkServer,
    diabetesController,
    liverController,
    kidneyController,
    parkinsonController,
    breastController

}


