import uvicorn 
from fastapi import FastAPI
import numpy as np 
import pickle 
import pandas as pd
from pydantic import BaseModel
import logging
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import math 


pregnancy_dict = {
    "no" : 0,
    "yes" : 1
}
behavior_dict = {
    "docile" : 0,
    "normal" : 1,
    "aggressive" : 2
}
gender_dict = {
    "female" : 0,
    "male" : 1
}

class GoatClass(BaseModel):
    MilkInLitres: int
    Age: int
    Height: int
    Weight: int
    Pregnancy: str
    Behavior: str
    Gender: str
    HayGrassIntake: int

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load model and preprocessor
logger.info("Loading model and preprocessor...")
with open("meat_quality_model.pkl", "rb") as f:
    meat_quality_model = pickle.load(f)
with open("milk_quality_model.pkl", "rb") as f:
    milk_quality_model = pickle.load(f)

# Index route
@app.get('/')
def index():
    logger.info("Received request on index route")
    return {'message': 'Team 64 NAAM_MAIN_KYA_RAKHA_HAI'}

# Prediction route
@app.get('/predict_meat_quality')
def predict_meat_quality(data: GoatClass):
    logger.info("Received prediction request")
    data = data.dict()
    milk_in_liters = data["MilkInLitres"]
    print("milk: " , milk_in_liters)
    age = data["Age"]
    print("age: " , age)
    height = data["Height"]
    print("height: " , height)
    weight = data["Weight"]
    print("weight: " , weight)
    pregnancy = pregnancy_dict[data["Pregnancy"]]
    print("pregnancy: " , pregnancy)
    behavior = behavior_dict[data["Behavior"]]
    print("behavior: " , behavior)
    gender = gender_dict[data["Gender"]]
    print("gender: " , gender)
    hay_grass_intake = data["HayGrassIntake"]
    print("hay grass index: " , hay_grass_intake)

    input_arr = [[milk_in_liters , age , height , weight , pregnancy , behavior , gender , hay_grass_intake]]
    prediction = meat_quality_model.predict(input_arr)
    result = math.ceil(prediction[0][0])
    if(result < 0):
        result = 0
    elif(result > 5):
        result = 5

    return {"prediction": result}


@app.get('/predict_milk_quality')
def predict_milk_quality(data: GoatClass):
    logger.info("Received prediction request")
    data = data.dict()
    milk_in_liters = data["MilkInLitres"]
    print("milk: " , milk_in_liters)
    age = data["Age"]
    print("age: " , age)
    height = data["Height"]
    print("height: " , height)
    weight = data["Weight"]
    print("weight: " , weight)
    pregnancy = pregnancy_dict[data["Pregnancy"]]
    print("pregnancy: " , pregnancy)
    behavior = behavior_dict[data["Behavior"]]
    print("behavior: " , behavior)
    gender = gender_dict[data["Gender"]]
    print("gender: " , gender)
    hay_grass_intake = data["HayGrassIntake"]
    print("hay grass index: " , hay_grass_intake)
    input_arr = [[milk_in_liters , age , height , weight , pregnancy , behavior , gender , hay_grass_intake]]
    prediction = milk_quality_model.predict(input_arr)

    result = math.ceil(prediction[0][0])
    if(result < 0):
        result = 0
    elif(result > 5):
        result = 5

    return {"prediction": result}