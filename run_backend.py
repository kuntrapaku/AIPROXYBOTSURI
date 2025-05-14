import os
import subprocess
import time
import requests
from config import INTELLIJ_PROJECT_PATH
from utils.logger import log_error

def run_backend():
    """ Start the backend server. """
    try:
        print(f"[DEBUG] Backend directory: {INTELLIJ_PROJECT_PATH}")

        # ✅ Build the project with Maven
        print("[INFO] Running: mvn clean install")
        build = subprocess.run(
            "mvn clean install",
            shell=True,
            capture_output=True,
            text=True,
            cwd=INTELLIJ_PROJECT_PATH
        )
        print(build.stdout)
        if build.returncode != 0:
            log_error("Backend build failed.")
            log_error(build.stderr)
            return False

        # ✅ Start Spring Boot in background
        print("[INFO] Starting Spring Boot backend...")
        backend_process = subprocess.Popen(
            "mvn spring-boot:run",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=INTELLIJ_PROJECT_PATH
        )

        # ✅ Wait for backend to start up (watch stdout)
        print("[INFO] Waiting for Spring Boot to start... (max 60s)")
        start_time = time.time()
        while time.time() - start_time < 60:
            line = backend_process.stdout.readline()
            if not line:
                break
            print(line.strip())

            if "Started" in line and "in" in line and "seconds" in line:
                print("[INFO] Backend is up and running!")
                return True

        log_error("Backend is not responding after waiting.")
        return False

    except Exception as e:
        log_error(f"Error in backend startup: {e}")
        return False
