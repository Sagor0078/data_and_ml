# ML Model to FastAPI Microservice  

This repository provides an **end-to-end guide** on converting raw data into a **Machine Learning (ML) model** and serving it as a **FastAPI microservice**.  

## Table of Contents    
- Data Preparation
- Train the ML Model 
- Build FastAPI Microservice
- Run & Test API
- Deployment 


---

## Overview  
This project demonstrates how to:  
- Load and preprocess data for ML models  
- Train a **scikit-learn** model and save it  
- Create a **FastAPI microservice** to serve predictions  
- Test the API using **cURL/Postman**  
- Deploy the service using **Docker**

## Run the server 
```bash
poetry run uvicorn api.classify:app --reload
```
- make request.sh executable
```bash
chmod +x request.sh
```
- run it
```bash
./request.sh
```








