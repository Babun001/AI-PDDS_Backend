import { Router } from "express";
import { upload } from "../middlewares/multer.middleware";


import liverController from "../controllers/liver.controller";
import diabetesController from "../controllers/diabetes.controller";
import kidneyController from "../controllers/kidney.controller";
import lungController from "../controllers/lung.controller";
import heartController from "../controllers/heart.controller";
import parkinsonController from "../controllers/parkinson.controller";
import breastController from "../controllers/breast.controller";
import imageUploader from "../controllers/imageUpload.controller";




const router = Router();

router.route("/diabetes-Detection").post(diabetesController);
router.route("/liver-Detection").post(liverController);
router.route("/kidney-Detection").post(kidneyController);
router.route("/parkinson-Detection").post(parkinsonController);
router.route("/breast-Detection").post(breastController);
router.route("/lung-Detection").post(lungController);
router.route("/heart-Detection").post(heartController);


router.route("/image-upload").post(upload.single("Image"), imageUploader);


export default router;