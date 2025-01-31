import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const heartController = asyncAwaitFunc(async (req, res) => {
    try {

        const {
            Age,
            Sex,
            ChestPainType,
            RestingBP,
            Cholesterol,
            FastingBS,
            RestingECG,
            MaxHR,
            ExerciseAngina,
            Oldpeak,
            ST_Slope
        } = req.body;

        const response = await axios.post("http://127.0.0.1:5000/heart",{
            Age,
            Sex,
            ChestPainType,
            RestingBP,
            Cholesterol,
            FastingBS,
            RestingECG,
            MaxHR,
            ExerciseAngina,
            Oldpeak,
            ST_Slope
        },{
            headers: {"Content-Type":"application/json"}
        })

        res.status(200).json({
            patientData: response.data
        })

    } catch (error: any) {
        throw new apiError(404, "error in heartController", error.message || "")
    }
})

export default heartController;