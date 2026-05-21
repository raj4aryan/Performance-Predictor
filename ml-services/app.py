from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = FastAPI()
predictor = PredictPipeline()

class StudentData(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: float
    writing_score: float

@app.get("/")
def home():
    return {"Message": "ML Services Running on port 8000"}

@app.post("/predict",)
def predict(data: StudentData):
    customData = CustomData(
        data.gender, 
        data.race_ethnicity, 
        data.parental_level_of_education, 
        data.lunch, 
        data.test_preparation_course, 
        data.reading_score,
        data.writing_score
    )

    df = customData.get_data_as_dataFrame()
    result = predictor.predict(df)

    return {"prediction" :float(result[0])}
