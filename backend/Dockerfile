FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default port for API
EXPOSE 8000
# Default port for syslog
EXPOSE 514/udp
