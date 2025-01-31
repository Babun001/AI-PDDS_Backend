import { Router } from "express";
import liverController from "../controllers/liver.controller"
import diabetesController from "../controllers/diabetes.controller"
import kidneyController from "../controllers/kidney.controller"




const router = Router();

router.route("/diabetes-Detection").post(diabetesController);
router.route("/liver-Detection").post(liverController);
router.route("/kidney-Detection").post(kidneyController);
router.route("/parkinson-Detection").post();
router.route("/breast-Detection").post();
// router.route("/").post();

export default router;