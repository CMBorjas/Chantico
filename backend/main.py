from fastapi import FastAPI
from api.routes import router
from database.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

from contextlib import asynccontextmanager
from receiver.syslog_server import start_syslog_server_bg, server_instance

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Start the UDP syslog server in a background thread
    syslog_thread = start_syslog_server_bg()
    yield
    # Shutdown: Stop the syslog server
    server_instance.stop()
    syslog_thread.join(timeout=2.0)

app = FastAPI(title="Chantico Agent API", description="Backend for the Digital Hearth Guardian", lifespan=lifespan)

app.include_router(router, prefix="/api")
