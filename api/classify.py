import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from schema.model_schema import ChurnPrediction
from loguru import logger

dotenv_path = os.path.join(os.path.dirname(__file__), "../config/.env")
load_dotenv(dotenv_path)

model_path = os.getenv("MODEL_PATH")

if not model_path:
    raise ValueError("MODEL_PATH is not set in the .env file")

logger.info(f"Loading model from: {model_path}")

try:
    with open(model_path, 'rb') as f_in:
        dv, model = pickle.load(f_in)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

app = FastAPI()

@app.post("/predict")
async def predict(customer: ChurnPrediction):
    logger.info("Received request for prediction")
    try:
        customer_dict = customer.dict()
        logger.debug(f"Customer input: {customer_dict}")

        # Transform the customer data and make prediction
        X = dv.transform([customer_dict])
        y_pred = model.predict_proba(X)[0, 1]
        churn = y_pred >= 0.5

        logger.info(f"Prediction made: churn_probability={y_pred}, churn={churn}")
        
        result = {
            'churn_probability': float(y_pred),
            'churn': bool(churn)
        }

        return JSONResponse(content=result)
    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})


