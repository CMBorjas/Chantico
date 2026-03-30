from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import models, database

router = APIRouter()

@router.get("/anomalies/")
def get_anomalies(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    anomalies = db.query(models.AnomalyLine).order_by(models.AnomalyLine.timestamp.desc()).offset(skip).limit(limit).all()
    return anomalies

@router.get("/health")
def health_check():
    return {"status": "ok", "service": "Chantico Backend"}
