import requests
from core.config import settings
import logging

logger = logging.getLogger(__name__)

def query_ollama(prompt: str, model: str = "llama3") -> str:
    """
    Synchronous query to local Ollama instance.
    """
    url = f"{settings.OLLAMA_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to query Ollama: {e}")
        return "Severity: Low\nAnalysis: Model offline or timeout.\nRecommendation: Check LLM service."
