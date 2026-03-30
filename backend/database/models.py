from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime, timezone
from database.database import Base

class AnomalyLine(Base):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    source_ip = Column(String(50), index=True)
    destination_ip = Column(String(50), index=True)
    protocol = Column(String(20))
    action = Column(String(50))
    raw_log = Column(Text)
    analysis = Column(Text)
    recommendation = Column(Text)
    severity = Column(String(20)) # Low, Medium, High, Critical
