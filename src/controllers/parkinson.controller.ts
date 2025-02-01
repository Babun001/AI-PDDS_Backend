import asyncAwaitFunc from "../utility/asyncAwaitFunc";
import apiError from "../utility/apiError";
import axios from "axios";

const parkinsonController = asyncAwaitFunc(async (req, res) => {
    try {
        const {
            mdvp_fo_hz,
            mdvp_fhi_hz,
            mdvp_flo_hz,
            mdvp_jitter_in_percent,
            mdvp_jitter_abs,
            mdvp_rap,
            mdvp_ppq,
            jitter_ddp,
            mdvp_shimmer,
            mdvp_shimmer_db,
            shimmer_apq3,
            shimmer_apq5,
            mdvp_apq,
            shimmer_dda,
            nhr,
            hnr,
            rpde,
            dfa,
            spread1,
            spread2,
            d2,
            ppe
        } = req.body;

        // console.table([{

        // }])

        const response = await axios.post("http://127.0.0.1:5000/parkinson",
            {
                mdvp_fo_hz,
                mdvp_fhi_hz,
                mdvp_flo_hz,
                mdvp_jitter_in_percent,
                mdvp_jitter_abs,
                mdvp_rap,
                mdvp_ppq,
                jitter_ddp,
                mdvp_shimmer,
                mdvp_shimmer_db,
                shimmer_apq3,
                shimmer_apq5,
                mdvp_apq,
                shimmer_dda,
                nhr,
                hnr,
                rpde,
                dfa,
                spread1,
                spread2,
                d2,
                ppe
            },
            {
                headers: { "Content-Type": "application/json" }
            }
        )

        res.status(200).json({
            patientData: response.data
        })

    } catch (error: any) {
        console.error("Error in parkinson controller", error);
        throw new apiError(404, "Error in parkinson controller", error.message || "")
    }
})

export default parkinsonController;