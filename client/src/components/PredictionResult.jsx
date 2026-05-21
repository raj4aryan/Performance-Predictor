function PredictionResult({ prediction }) {
    return (
        <div className="prediction-card">
            <h2>Predicted Math Score</h2>
            <p>{prediction}</p>
        </div>
    )
}

export default PredictionResult