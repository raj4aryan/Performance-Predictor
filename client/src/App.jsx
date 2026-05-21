import { useState } from "react"
import StudentForm from "./components/StudentForm"
import PredictionResult from "./components/PredictionResult"
import { predictPerformance } from "./services/predictionApi"

function App() {
    const [prediction, setPrediction] = useState(null)
    const handlePrediction = async (formData) => {
        try {
            const result = await predictPerformance(formData)
            setPrediction(result.prediction)
        }
        catch (error) {
            console.log(error)
        }
    }
    return (
        <div className="app-container">
            <div className="main-card">
                <h1>Student Performance Predictor</h1>
                <p className="subtitle">
                    Predict student math performance using ML
                </p>
                <StudentForm onPredict={handlePrediction} />
                {
                    prediction &&
                    <PredictionResult prediction={prediction} />
                }
            </div>
        </div>
    )
}
export default App