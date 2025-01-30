import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const liverController = asyncAwaitFunc(async (req, res) => {
    try {
        const { Age,
            Gender,
            Total_Bilirubin,
            Alamine_Aminotransferase,
            Aspartate_Aminotransferase,
            Total_Proteins,
            Albumin,
            Albumin_and_Globulin_Ratio } = req.body;

        const response = await axios.post("http://127.0.0.1:5000/liver", {
            Age,
            Gender,
            Total_Bilirubin,
            Alamine_Aminotransferase,
            Aspartate_Aminotransferase,
            Total_Proteins,
            Albumin,
            Albumin_and_Globulin_Ratio
        },
            {
                headers: { "Content-Type": "application/json" }
            }

        )
        if (!response) {
            throw new apiError(404, "Response not found!!", "")
        }

        console.log(response.data);

        res.status(200).json({
            message:"Received Paitent data",
            data:response.data
        })
        

        res.status(201).json({ message: "data received" })

    } catch (error) {
        console.error("Error in LiverController:", error);
        throw new apiError(404, "bad request in liverController", "")
    }
})

export default liverController;