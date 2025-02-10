import { Router } from "express";
import { upload } from "../middlewares/multer.middleware";


import liverController from "../controllers/liver.controller";
import diabetesController from "../controllers/diabetes.controller";
import kidneyController from "../controllers/kidney.controller";
import lungController from "../controllers/lung.controller";
import heartController from "../controllers/heart.controller";
import parkinsonController from "../controllers/parkinson.controller";
import breastController from "../controllers/breast.controller";
import strokeController from "../controllers/stroke.controller"

import alzheimer_controller from "../controllers/alzheimer.controller";
import tuberculosis_controller from "../controllers/tuberculosis.controller";



const router = Router();

router.route("/diabetes-Detection").post(diabetesController);
router.route("/liver-Detection").post(liverController);
router.route("/kidney-Detection").post(kidneyController);
router.route("/parkinson-Detection").post(parkinsonController);
router.route("/breast-Detection").post(breastController);
router.route("/lung-Detection").post(lungController);
router.route("/heart-Detection").post(heartController);
router.route("/stroke-Detection").post(strokeController);


router.route("/scanning-Alzheimer").post(upload.single("Image"), alzheimer_controller);
router.route("/scanning-Tuberculosis").post(upload.single("Image"), tuberculosis_controller);


export default router;