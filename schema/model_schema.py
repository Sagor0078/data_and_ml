"""Schema for Churn Prediction Model."""

from pydantic import BaseModel
from typing import Literal

class ChurnPrediction(BaseModel):

    
    gender: Literal["male", "female"]
    seniorcitizen: int
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["yes", "no", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["yes", "no"]
    onlinebackup: Literal["yes", "no"]
    deviceprotection: Literal["yes", "no"]
    techsupport: Literal["yes", "no"]
    streamingtv: Literal["yes", "no"]
    streamingmovies: Literal["yes", "no"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal["electronic_check", "mailed_check", "bank_transfer", "credit_card"]
    tenure: int
    monthlycharges: float
    totalcharges: float
