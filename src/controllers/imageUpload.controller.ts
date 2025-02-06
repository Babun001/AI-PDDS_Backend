import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import uploadImageToColudinary from "../utility/cloudinaryUpload.utility";
import apiError from "../utility/apiError";

const imageUploader = asyncAwaitFunc(async(req,res) =>{
    try {
        const fileName = req.file?.path;

        if(!fileName) {
            throw new apiError(404,"ImageFile not Found!","")
        }

        const uploadedToCloudinary = await uploadImageToColudinary(fileName)

        if(!uploadedToCloudinary){
            throw new apiError(400,"Failed To upload to cloudinary","")
        }

        // console.log("cloudinary links",uploadedToCloudinary);

        
        
        
        return res
        .status(200).json({
            patientImage : uploadedToCloudinary?.url
        })
        
    } catch (error:any) {
        console.error("error on imageUploader "+ error);
        return res.status(500).json({ error: "Server Error: " + error.message });

    }
})

export default imageUploader;