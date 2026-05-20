import os
import sys
import pandas as pd
from src.exceptions import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            modelPath = os.path.join("artifacts", "model.pkl")
            preprocessorPath = os.path.join("artifacts", "preprocessor.pkl")
            model = load_object(file_path = modelPath)
            preprocessor = load_object(file_path = preprocessorPath)
            scaledData = preprocessor.transform(features)
            y_pred = model.predict(scaledData)
            return y_pred
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course,math_score,reading_score ,writing_score):
        self.gender= gender
        self.race_ethnicity= race_ethnicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch = lunch 
        self.test_preparation_course= test_preparation_course
        self.math_score= math_score
        self.reading_score= reading_score
        self.writing_score= writing_score

    def get_data_as_dataFrame(self):
        try:
            data = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "math_score": [self.math_score],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(data=data)
        except Exception as e:
            raise CustomException(e, sys)
