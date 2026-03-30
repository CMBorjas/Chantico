import socket
import logging
import threading
from worker.tasks import analyze_syslog_message
from core.config import settings

logger = logging.getLogger(__name__)

class SyslogServer:
    def __init__(self, host="0.0.0.0", port=514):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = False
    
    def start(self):
        self.running = True
        try:
            self.sock.bind((self.host, self.port))
            logger.info(f"Syslog server listening on {self.host}:{self.port}/udp")
            while self.running:
                try:
                    self.sock.settimeout(1.0) # To allow checking self.running
                    data, addr = self.sock.recvfrom(4096)
                    message = data.decode("utf-8", errors="ignore").strip()
                    # Send to Celery worker immediately so we don't block
                    analyze_syslog_message.delay(message, addr[0])
                except socket.timeout:
                    continue
        except Exception as e:
            if self.running: # Only log if it wasn't intentionally stopped
                logger.error(f"Error in syslog server: {e}")
        finally:
            self.sock.close()

    def stop(self):
        self.running = False

server_instance = SyslogServer(host=settings.SYSLOG_HOST, port=settings.SYSLOG_PORT)

def start_syslog_server_bg():
    thread = threading.Thread(target=server_instance.start, daemon=True)
    thread.start()
    return thread
