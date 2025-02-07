import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import uploadImageToCloudinary from "../utility/cloudinaryUpload.utility";
import apiError from "../utility/apiError";
import axios from "axios";

const imageUploader = asyncAwaitFunc(async(req,res) =>{
    try {
        const fileName = req.file?.path;

        if(!fileName) {
            throw new apiError(404,"ImageFile not Found!","")
        }

        const uploadedToCloudinary = await uploadImageToCloudinary(fileName)

        if(!uploadedToCloudinary){
            throw new apiError(400,"Failed To upload to cloudinary","")
        }

        const imgLink = uploadedToCloudinary?.url || "";

        if (!imgLink.startsWith("http")) {
            throw new apiError(400, "Invalid Cloudinary URL", "");
        }

        const response = await axios.post("http://127.0.0.1:5000/alzheimer", {imgLink}, { headers:{"Content-Type":"application/json"}} )
        
        // console.log(response.data);
        
        return res.status(200).json(response.data);
        
    } catch (error:any) {
        console.error("error on imageUploader "+ error);
        return res.status(500).json({ error: "Server Error: " + error.message });

    }
})

export default imageUploader;