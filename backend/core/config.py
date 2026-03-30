import os

class Settings:
    PROJECT_NAME: str = "Chantico"
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./chantico.db")
    SYSLOG_HOST: str = os.getenv("SYSLOG_HOST", "0.0.0.0")
    SYSLOG_PORT: int = int(os.getenv("SYSLOG_PORT", 514))

settings = Settings()
