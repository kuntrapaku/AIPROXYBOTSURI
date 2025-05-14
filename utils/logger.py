import os
import time

LOG_FILE = "logs/error.log"

def log_error(message):
    """ Log error messages to a file. """
    os.makedirs("logs", exist_ok=True)  # Ensure the logs directory exists
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(f"[ERROR] {message}")
