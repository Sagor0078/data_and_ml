import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../config/.env")
load_dotenv(dotenv_path)

model_path = os.getenv("MODEL_PATH")

if not model_path:
    raise ValueError("MODEL_PATH is not set in the .env file")

# Load the model
with open(model_path, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI()

class Customer(BaseModel):
    gender: str
    seniorcitizen: int
    partner: str
    dependents: str
    phoneservice: str
    multiplelines: str
    internetservice: str
    onlinesecurity: str
    onlinebackup: str
    deviceprotection: str
    techsupport: str
    streamingtv: str
    streamingmovies: str
    contract: str
    paperlessbilling: str
    paymentmethod: str
    tenure: int
    monthlycharges: float
    totalcharges: float

@app.post("/predict")
async def predict(customer: Customer):
    customer_dict = customer.dict()
    X = dv.transform([customer_dict])
    
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return JSONResponse(content=result)

