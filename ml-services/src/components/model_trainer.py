import sys
import os
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    
    def __init__(self):
        self.model_file_path = ModelTrainerConfig().model_file_path
    
    def initiate_model_training(self, train_data_arr, test_data_arr):
        try:
            X_train, X_test, y_train, y_test = (
                train_data_arr[:,:-1],
                test_data_arr[:,:-1],
                train_data_arr[:,-1],
                test_data_arr[:,-1]
            )

            models = {
                "LinearRegression": LinearRegression(),
                "KNeighborsRegressor": KNeighborsRegressor(), 
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoostRegressor": CatBoostRegressor(verbose=False)
            }

            model_report: dict = evaluate_models(X_train = X_train, y_train = y_train, X_test=X_test, y_test = y_test, models = models)

            logging.info("Model Training Completed")

            best_model_score = max(model_report.values())
            if(best_model_score < 0.6):
                raise CustomException("Model is WEAK", sys)

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            save_object(
                filePath=self.model_file_path,
                obj=best_model
            )
            logging.info("Best Model found and saved")

            predicted = best_model.predict(X_test)
            score = r2_score(y_test, predicted)
            return best_model_name, score

        except Exception as e:
            raise CustomException(e, sys)
