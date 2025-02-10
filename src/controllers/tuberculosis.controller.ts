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




        console.log(upload_to_cloudinary?.url);
        res.status(200).json({
            message: "data received"
        })
        
    } catch (error:any) {
        console.error(error.message);
        throw new apiError(400,"Unable to upload Image || error in tuberculosis_controller", "")
    }
})

export default tuberculosis_controller;