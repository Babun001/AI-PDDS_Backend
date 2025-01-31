import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const kidneyController = asyncAwaitFunc(async (req, res) => {
    try {
        const {
            age,
            blood_pressure,
            specific_gravity,
            albumin,
            sugar,
            blood_glucose_random,
            blood_urea,
            serum_creatinine,
            sodium,
            potassium,
            haemoglobin,
            packed_cell_volume,
            white_blood_cell_count,
            red_blood_cell_count
        } = req.body;

        const response = await axios.post('http://127.0.0.1:5000/kidney',
            {
                age,
                blood_pressure,
                specific_gravity,
                albumin,
                sugar,
                blood_glucose_random,
                blood_urea,
                serum_creatinine,
                sodium,
                potassium,
                haemoglobin,
                packed_cell_volume,
                white_blood_cell_count,
                red_blood_cell_count
            },
            {
                headers: { "Content-Type": "Application/json" }
            }
        )

        if (!response) {
            throw new apiError(404, "Unable to received data from kidney api!", "");
        }

        // const response = new Promise(async (resolved, rejected) => {
        //     await axios.post('http://127.0.0.1:5000/kidney',
        //         {
        //             age,
        //             blood_pressure,
        //             specific_gravity,
        //             albumin,
        //             sugar,
        //             blood_glucose_random,
        //             blood_urea,
        //             serum_creatinine,
        //             sodium,
        //             potassium,
        //             haemoglobin,
        //             packed_cell_volume,
        //             white_blood_cell_count,
        //             red_blood_cell_count
        //         },
        //         {
        //             headers: { "Content-Type": "Application/json" }
        //         }
        //     )
        // })

        res.status(200).json({
            paitentData: response.data
        })
    } catch (error) {
        console.error("Error in kidney controller" + error);
        throw new apiError(404, "Error in kidney controller", "");
    }

})

export default kidneyController;