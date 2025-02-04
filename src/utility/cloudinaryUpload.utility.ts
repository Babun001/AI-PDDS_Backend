import { v2 as cloudinary } from 'cloudinary';
import fs from 'fs'


cloudinary.config({
    cloud_name: process.env.CloudName,
    api_key: process.env.APIKey,
    api_secret: process.env.APISecret
})

const uploadImageToColudinary = async(localFilePath:string) =>{
    try {
        if(!localFilePath) return null;
        const response = await cloudinary.uploader.upload(localFilePath, {resource_type: 'auto'});

        console.log(response);

        fs.unlinkSync(localFilePath)
        console.log(`unlinkSync method deleted file successfully`);
        
        

    } catch (error:any) {
        console.error("Error in cloudinary module!! ", error.message || "");
        fs.unlink(localFilePath, err =>{
            if (err) {
                console.error("Error deleting file:", err);
            } else {
                console.log("File deleted successfully!");
            }
        })
    }
}

export default uploadImageToColudinary;