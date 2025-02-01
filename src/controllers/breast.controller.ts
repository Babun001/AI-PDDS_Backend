import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const breastController = asyncAwaitFunc(async (req, res) => {
    try {

        if (!req.body) {
            throw new apiError(400, "Request body not found!!", "")
        }

        const {
            radius_mean,
            texture_mean,
            perimeter_mean,
            area_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            concave_points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            radius_se,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            concave_points_se,
            symmetry_se,
            fractal_dimension_se,
            radius_worst,
            texture_worst,
            perimeter_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            concave_points_worst,
            symmetry_worst,
            fractal_dimension_worst

        } = req.body;

        const response = await axios.post("http://127.0.0.1:5000/breast",
            {
                radius_mean,
                texture_mean,
                perimeter_mean,
                area_mean,
                smoothness_mean,
                compactness_mean,
                concavity_mean,
                concave_points_mean,
                symmetry_mean,
                fractal_dimension_mean,
                radius_se,
                texture_se,
                perimeter_se,
                area_se,
                smoothness_se,
                compactness_se,
                concavity_se,
                concave_points_se,
                symmetry_se,
                fractal_dimension_se,
                radius_worst,
                texture_worst,
                perimeter_worst,
                area_worst,
                smoothness_worst,
                compactness_worst,
                concavity_worst,
                concave_points_worst,
                symmetry_worst,
                fractal_dimension_worst
            },
            {
                headers: { "Content-Type": "application/json" }
            }
        )

        res.status(200).json({
            patientData: response.data
        })


    } catch (error: any) {
        console.error("Error in breast Prediction controller", error);
        throw new apiError(400, "Error in Breast Prediction Controller", error.message || "")
    }
})

export default breastController;