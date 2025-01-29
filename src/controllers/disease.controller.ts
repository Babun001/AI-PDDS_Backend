import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const checkServer = asyncAwaitFunc((req,res) =>{
    try {
        res.status(201).json({
            message:"all okay"
        })
    } catch (error) {
        
    }
})

const diabetesController = asyncAwaitFunc(async(req,res) =>{
    try {
        const queryParams = req.query;
        console.log("Patient data ==> ", queryParams);

        // this is flaskApi to fetch patient status based on data(queryParams)
        const predictedValue = await axios.get(`http://127.0.0.1:5000/diabetes`,{
            params:queryParams
        });

        console.log(predictedValue.data);
        
        res.status(200).json(predictedValue.data);
        
    } catch (error:any) {
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
        throw new apiError(404,"bad request in liverController","")
    }
})

const kidneyController = asyncAwaitFunc((req, res) => {
    try {
        res.status(202).json({
            mess: "kidneyController"
        })
    } catch (error) {
        throw new apiError(404,"bad request in kidneyController","")
    }
})

const parkinsonController = asyncAwaitFunc((req, res) => {
    try {
        const queryParams = req.query;
        // console.log(queryParams);

        res.status(200).json(queryParams)
    } catch (error) {
        throw new apiError(404,"bad request in parkinsonController","")
    }
})

const breastController = asyncAwaitFunc((req, res) => {
    try {
        const queryParams = req.query;
        // console.log(queryParams);

        res.status(200).json(queryParams)
    } catch (error) {
        throw new apiError(404,"bad request in breastController","")
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


