const {predictPerformance} = require("../services/mlservice")

const predict = async(req, res)=>{
    try {
        const prediction = await predictPerformance(req.body)
        return res.status(200).json(prediction)
    } catch (error) {
        res.status(500).json({
            message: 'Prediction failed',
            error: error.message
        })
    }
}

module.exports = {predict}