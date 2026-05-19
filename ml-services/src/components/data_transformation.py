import os
import sys

import pandas as pd
import numpy as np

from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformConfig:
    preprocessor_file_path: str=os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformConfig()
    
    def get_data_transformed_object(self):
        try:
            numFeatures = ["reading score",	"writing score"]
            categFeatures = ["gender", "race/ethnicity", "parental level of education",	"lunch", "test preparation course"]

            numPipeline = Pipeline(
                steps=[
                    ("Impute", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            categPipeline = Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy='most_frequent')),
                    ("OHE", OneHotEncoder())
                ]
            )
            preprocessor = ColumnTransformer([
                ("numPipeline", numPipeline, numFeatures),
                ("categPipeline",categPipeline, categFeatures)
            ])
            logging.info("Preprocessor created")
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, trainPath, testPath):
        try:
            traindf = pd.read_csv(trainPath)
            testdf = pd.read_csv(testPath)
            
            target_feature = 'math score'
            numFeatures = ["reading score",	"writing score"]

            input_feature_train_df = traindf.drop(columns=[target_feature])
            target_feature_train_df = traindf[target_feature]

            input_feature_test_df = testdf.drop(columns=[target_feature])
            target_feature_test_df = testdf[target_feature]

            preprocessingObj = self.get_data_transformed_object()
            logging.info("Ready for Preprocessing")

            input_feature_train_arr = preprocessingObj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessingObj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Preprocessing completed")

            save_object(
                filePath = self.data_transformation_config.preprocessor_file_path,
                obj = preprocessingObj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)