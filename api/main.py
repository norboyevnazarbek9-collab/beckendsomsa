from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Dict

app = FastAPI()

# Frontend ulanishi uchun CORS ni ochamiz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vaqtinchalik xotira (Ma'lumotlar bazasi vazifasida)
db = {
    "users": [],
    "somsaTypes": [
        {"id": 1, "name": "Mol go'shtli", "price": 10000},
        {"id": 2, "name": "Qo'y go'shtli", "price": 12000},
        {"id": 3, "name": "Avashnoy", "price": 6000},
        {"id": 4, "name": "Qiyma", "price": 8000},
        {"id": 5, "name": "Kartoshkali", "price": 5000},
        {"id": 6, "name": "Qovoqli", "price": 5000},
        {"id": 7, "name": "Tovuqli", "price": 8000}
    ],
    "productionLogs": [],
    "salesLogs": [],
    "auditRequests": [],
    "cardNumber": ""
}

class DataModel(BaseModel):
    data: Any

@app.get("/api/data")
def get_data():
    return db

@app.post("/api/users")
def save_users(payload: Dict[str, Any]):
    db["users"] = payload.get("users", [])
    return {"success": True}

@app.post("/api/somsa-types")
def save_somsa(payload: Dict[str, Any]):
    db["somsaTypes"] = payload.get("somsaTypes", [])
    return {"success": True}

@app.post("/api/production-logs")
def save_production(payload: Dict[str, Any]):
    db["productionLogs"] = payload.get("productionLogs", [])
    return {"success": True}

@app.post("/api/sales-logs")
def save_sales(payload: Dict[str, Any]):
    db["salesLogs"] = payload.get("salesLogs", [])
    return {"success": True}

@app.post("/api/audit-requests")
def save_audit(payload: Dict[str, Any]):
    db["auditRequests"] = payload.get("auditRequests", [])
    return {"success": True}

@app.post("/api/card-number")
def save_card(payload: Dict[str, Any]):
    db["cardNumber"] = payload.get("cardNumber", "")
    return {"success": True}
