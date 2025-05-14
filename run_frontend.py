import os
import time
import subprocess
from utils.logger import log_error
from utils.process_manager import kill_process_by_port, execute_command
from utils.emulator_manager import start_emulator
from config import REACT_NATIVE_PATH

def run_frontend():
    """
    Start the frontend React Native app and emulator.
    """
    try:
        print("\n--- Starting Frontend ---")
        print(f"[INFO] Using React Native path: {REACT_NATIVE_PATH}")


        # ✅ Start the emulator
        if not start_emulator("Pixel_7a_API_35"):
            log_error("Emulator startup failed.")
            return False

        # ✅ Kill Metro if already running
        kill_process_by_port(8081)

        # ✅ Start Metro using Popen (so it stays alive)
        print("[INFO] Starting Metro Bundler...")
        subprocess.Popen("npx react-native start", shell=True, cwd=REACT_NATIVE_PATH)


        # ⏱ Give Metro some time to initialize
        time.sleep(10)

        # ✅ Build and launch the Android app
        print("[INFO] Building and running the app on Android...")
        run_android = subprocess.run("npx react-native run-android", shell=True, capture_output=True, text=True, cwd=REACT_NATIVE_PATH)
        print("STDOUT:\n", run_android.stdout)
        print("STDOUT:\n", run_android.stderr)
        if run_android.returncode != 0:
            log_error("React Native app failed to start.")
            log_error(run_android.stderr)
            return False

        print("[INFO] Frontend is now running.")
        return True

    except Exception as e:
        log_error(f"Error in frontend startup: {e}")
        return False
