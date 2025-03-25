import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from fastapi.responses import JSONResponse

# Load the model and vectorizer
model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Define FastAPI app
app = FastAPI()

# Define input data structure using Pydantic
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

# Prediction route
@app.post("/predict")
async def predict(customer: Customer):
    # Convert the customer data to the appropriate format for the model
    customer_dict = customer.dict()
    X = dv.transform([customer_dict])
    
    # Predict the churn probability
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return JSONResponse(content=result)

# Run the application (use `uvicorn` for production)
# If running locally for development, use `uvicorn`:
# uvicorn app_name:app --reload
