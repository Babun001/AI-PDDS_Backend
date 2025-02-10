import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import uploadImageToColudinary from "../utility/cloudinaryUpload.utility"
import axios  from "axios";

const tuberculosis_controller = asyncAwaitFunc(async(req,res) =>{
    try {
        const fileName = req.file?.path;

        if(!fileName){
            throw new apiError(404, "file not received!", "");
        }

        const upload_to_cloudinary =await uploadImageToColudinary(fileName);

        if(!upload_to_cloudinary) {
            throw new apiError(400, "upload failed in cloudinary!", "");
        }

        const cloudinaryImageLink = upload_to_cloudinary?.url || ""

        if(!cloudinaryImageLink.startsWith("http")){
            throw new apiError(400, "URL is not ready yet!!", "")
        }

        const response = await axios.post("http://127.0.0.1:5000/tuberculosis",
            {
                cloudinaryImageLink
            },

            {
                headers:{"Content-Type" : "application/json"}
            }
        )

        res.status(200).json({
            patientCondition : response.data
        })
        
    } catch (error:any) {
        console.error(error.message);
        throw new apiError(400,"Unable to upload Image || error in tuberculosis_controller", "")
    }
})

export default tuberculosis_controller;