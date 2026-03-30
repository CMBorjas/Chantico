import logging
from worker.celery_app import celery_app
from core.llm_client import query_ollama
from database.database import SessionLocal
from database.models import AnomalyLine

logger = logging.getLogger(__name__)

@celery_app.task(bind=True, max_retries=3)
def analyze_syslog_message(self, raw_message: str, source_ip: str = "unknown"):
    """
    Parses the raw syslog message, queries the LLM to determine if it's anomalous,
    and stores the result if the LLM flags it.
    """
    try:
        prompt = f"""
You are Chantico, a network security AI. 
Analyze the following OPNsense syslog message. 
Determine if it represents a threat, an anomaly, or benign traffic.
Log: {raw_message}

Provide your response in the following format:
Severity: [Low, Medium, High, Critical, Benign]
Analysis: [Brief explanation of what the log means and why]
Recommendation: [What action should be taken, if any]
        """
        
        response = query_ollama(prompt)
        
        severity = "Unknown"
        analysis = ""
        recommendation = ""
        
        for line in response.splitlines():
            line_str = line.strip()
            if line_str.startswith("Severity:"):
                severity = line_str.split(":", 1)[1].strip()
            elif line_str.startswith("Analysis:"):
                analysis = line_str.split(":", 1)[1].strip()
            elif line_str.startswith("Recommendation:"):
                recommendation = line_str.split(":", 1)[1].strip()
        
        if severity.lower() != "benign":
            db = SessionLocal()
            try:
                anomaly = AnomalyLine(
                    source_ip=source_ip,
                    raw_log=raw_message,
                    analysis=analysis,
                    recommendation=recommendation,
                    severity=severity
                )
                db.add(anomaly)
                db.commit()
            except Exception as e:
                logger.error(f"DB Error: {e}")
            finally:
                db.close()
                
        return {"status": "success", "severity": severity}
    except Exception as exc:
        logger.error(f"Error analyzing syslog message: {exc}")
        raise self.retry(exc=exc, countdown=5)
