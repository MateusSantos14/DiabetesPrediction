from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware 
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class Input(BaseModel):
    Gender: int
    AGE: int
    Urea: float
    Cr: float
    HbA1c: float
    Chol: float
    TG: float
    HDL: float
    LDL: float
    VLDL: float
    BMI: float


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


NUMERICAL_COLS = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
GENDER_COLS = ['Gender_0', 'Gender_1'] 
@app.post('/predict')
async def predict(input: Input):
    """
    Endpoint para realizar predições usando um modelo pré-treinado.
    O dado de entrada é pré-processado com Z-score e PCA antes da predição.
    """
    try:
        prediction_model = load('best_model.pkl')

    except FileNotFoundError as e:
        return {"error": f"Erro ao carregar o modelo: {e}. Verifique se os arquivos .pkl e .joblib estão no diretório correto."}

    logger.debug(prediction_model)

    data_dict = input.model_dump()

    if data_dict['Gender'] == 0:
        gender_encoded = [1, 0] 
    else: 
        gender_encoded = [0, 1] 

    numerical_data = [data_dict[col] for col in NUMERICAL_COLS]

    full_data = numerical_data + gender_encoded

    data = np.array(full_data).reshape(1, -1)

    print(data)
    
    prediction = prediction_model.predict(data)

    return {"prediction": prediction[0].item()}
