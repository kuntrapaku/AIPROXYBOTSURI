import time
import requests
import subprocess
from utils.logger import log_error

BACKEND_URL = "http://localhost:8080/api/chat/ask"
FRONTEND_PORT = 8081

def monitor_services():
    """
    Monitor backend and frontend services continuously.
    Logs status every 15 seconds.
    """
    while True:
        # Check Backend
        try:
            response = requests.get(BACKEND_URL)
            if response.status_code == 200:
                print("[INFO] Backend is running.")
            else:
                log_error(f"Backend returned status: {response.status_code}")
        except requests.RequestException as e:
            log_error(f"Backend check error: {e}")

        # Check Frontend (Metro Bundler on port 8081)
        try:
            result = subprocess.run(
                f'netstat -ano | findstr :{FRONTEND_PORT}',
                shell=True,
                capture_output=True,
                text=True
            )
            if str(FRONTEND_PORT) in result.stdout:
                print("[INFO] Frontend is running.")
            else:
                log_error("Frontend is not running.")
        except Exception as e:
            log_error(f"Frontend check error: {e}")

        time.sleep(15)
