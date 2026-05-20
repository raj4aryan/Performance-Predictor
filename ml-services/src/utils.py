import os
import sys
import dill
from src.exceptions import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(filePath, obj):
    try:
        dirPath = os.path.dirname(filePath)
        os.makedirs(dirPath, exist_ok=True)

        with open(filePath, "wb") as f:
            dill.dump(obj, f)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for modelName, model in models.items():

            criteria = params[modelName]
            grid = GridSearchCV(estimator=model, param_grid=criteria, n_jobs=-1, cv=4)

            grid.fit(X_train, y_train)
            model.set_params(**grid.best_params_)
            model.fit(X_train, y_train)

            #evaluation
            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)
            report[modelName] = score
        
        return report
    
    except Exception as e:
        raise CustomException(e, sys)
