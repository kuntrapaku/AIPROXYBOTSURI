# utils/process_manager.py

import subprocess
from utils.logger import log_error

RETRY_LIMIT = 2  # Default retry limit

def kill_process_by_port(port):
    """ Kill process listening on the given port """
    # ... existing logic ...

def execute_command(command, retries=0):
    """ Execute a shell command with optional retries. """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr

        if "BUILD FAILURE" in output or "Exception" in output or "Error" in output:
            if "BUILD SUCCESS" not in output:
                if retries < RETRY_LIMIT:
                    print(f"[INFO] Retrying command: {command} (Attempt {retries + 1})")
                    return execute_command(command, retries + 1)
                else:
                    log_error(f"Command failed after {RETRY_LIMIT} attempts: {command}")
                    return False

        print(output)
        return True

    except Exception as e:
        log_error(f"Command execution error: {e}")
        return False
