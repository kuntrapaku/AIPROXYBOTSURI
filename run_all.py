import os
import subprocess
import time
from utils.logger import log_error, log_info
from run_backend import run_backend
from run_frontend import run_frontend

def cleanup():
    """
    Clean up all running processes (Emulator, Node.js, Java) and ADB server.
    """
    log_info("Starting cleanup process...")

    # Terminate Emulator processes
    try:
        result = subprocess.run("tasklist | findstr emulator", shell=True, capture_output=True, text=True)
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                pid = line.split()[1]
                log_info(f"Terminating Emulator process PID: {pid}")
                subprocess.run(f"taskkill /F /PID {pid}", shell=True)
        else:
            log_info("No emulator processes found.")
    except Exception as e:
        log_error(f"Error terminating emulator processes: {e}")

    # Terminate Node.js processes
    try:
        subprocess.run("taskkill /F /IM node.exe", shell=True)
        log_info("Terminated all Node.js processes.")
    except Exception as e:
        log_error(f"Error terminating Node.js processes: {e}")

    # Terminate Java processes
    try:
        subprocess.run("taskkill /F /IM java.exe", shell=True)
        log_info("Terminated all Java processes.")
    except Exception as e:
        log_error(f"Error terminating Java processes: {e}")

    # Kill ADB server
    try:
        subprocess.run("adb kill-server", shell=True)
        log_info("ADB server terminated.")
    except Exception as e:
        log_error(f"Error terminating ADB server: {e}")

    log_info("Cleanup process completed successfully.")

def run_all():
    """
    Run backend, frontend, and monitor services sequentially.
    """
    try:
        log_info("Starting services...")

        # Start backend
        run_backend()

        # Start frontend
        run_frontend()

        log_info("All services started successfully.")

    except Exception as e:
        log_error(f"Error in running services: {e}")
        cleanup()

if __name__ == "__main__":
    # Before starting, perform cleanup to avoid conflicts
    cleanup()

    # Start all services
    run_all()
