import os
import sys
import dill
from src.exceptions import CustomException

def save_object(filePath, obj):
    try:
        dirPath = os.path.dirname(filePath)
        os.makedirs(dirPath, exist_ok=True)

        with open(filePath, "wb") as f:
            dill.dump(obj, f)
    except Exception as e:
        raise CustomException(e, sys)