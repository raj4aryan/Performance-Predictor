const axios = require("axios")

const predictPerformance = async(studentData)=>{
    try {
        const response = await axios.post(
            'http://127.0.0.1:8000/predict',
            studentData
        )
        return response.data
    } catch (error) {
        console.error(error)
    }
}

module.exports = {predictPerformance}