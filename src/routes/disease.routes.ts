import { Router } from "express";
import {
    diabetesController,
    liverController,
    kidneyController,
    parkinsonController,
    breastController,
    checkServer
}
from '../controllers/disease.controller'



const router = Router();

router.route("/diabetes-Detection").post(diabetesController);
router.route("/liver-Detection").post(liverController);
router.route("/kidney-Detection").post(kidneyController);
router.route("/parkinson-Detection").post(parkinsonController);
router.route("/breast-Detection").post(breastController);
router.route("/").post(checkServer);

export default router;