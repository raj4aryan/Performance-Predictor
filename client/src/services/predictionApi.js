import axios from "axios"
const API_URL = "http://localhost:3500/predict"

export const predictPerformance = async(studentData)=>{
    try {
        const response = await axios.post(
            API_URL,
            studentData
        )
        return response.data
    } catch (error) {
        console.log(error)
        throw error
    }
}