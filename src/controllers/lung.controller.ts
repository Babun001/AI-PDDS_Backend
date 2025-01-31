import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const lungController = asyncAwaitFunc(async (req, res) => {
    try {
        const {
            Age,
            Gender,
            Air_Pollution,
            Alcohol_use,
            Dust_Allergy,
            OccuPational_Hazards,
            Genetic_Risk,
            chronic_Lung_Disease,
            Balanced_Diet,
            Obesity,
            Smoking,
            Passive_Smoker,
            Chest_Pain,
            Coughing_of_Blood,
            Fatigue,
            Weight_Loss,
            Shortness_of_Breath,
            Wheezing,
            Swallowing_Difficulty,
            Clubbing_of_Finger_Nails,
            Frequent_Cold,
            Dry_Cough,
            Snoring
        }
            = req.body;
        console.table([{
            Age,
            Gender,
            Air_Pollution,
            Alcohol_use,
            Dust_Allergy,
            OccuPational_Hazards,
            Genetic_Risk,
            chronic_Lung_Disease,
            Balanced_Diet,
            Obesity,
            Smoking,
            Passive_Smoker,
            Chest_Pain,
            Coughing_of_Blood,
            Fatigue,
            Weight_Loss,
            Shortness_of_Breath,
            Wheezing,
            Swallowing_Difficulty,
            Clubbing_of_Finger_Nails,
            Frequent_Cold,
            Dry_Cough,
            Snoring
        }]);


        const response = await axios.post("http://127.0.0.1:5000/lung",
            {
                Age,
                Gender,
                Air_Pollution,
                Alcohol_use,
                Dust_Allergy,
                OccuPational_Hazards,
                Genetic_Risk,
                chronic_Lung_Disease,
                Balanced_Diet,
                Obesity,
                Smoking,
                Passive_Smoker,
                Chest_Pain,
                Coughing_of_Blood,
                Fatigue,
                Weight_Loss,
                Shortness_of_Breath,
                Wheezing,
                Swallowing_Difficulty,
                Clubbing_of_Finger_Nails,
                Frequent_Cold,
                Dry_Cough,
                Snoring
            },
            {
                headers: { "Content-Type": "application/json" }
            }
        )

        res.status(200).json({
            patientData: response.data
        })


    } catch (error) {
        throw new apiError(404, "lungController is not working...!!", "")
    }
})

export default lungController;