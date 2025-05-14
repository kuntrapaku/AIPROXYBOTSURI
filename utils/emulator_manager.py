import subprocess
import time
from utils.logger import log_error

def start_emulator(avd_name):
    """
    Start the Android Emulator with the given AVD name if not already running.
    """
    try:
        result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
        if "emulator" not in result.stdout:
            print(f"[INFO] Starting emulator: {avd_name}")
            emulator_path = r"C:\Users\suri2\AppData\Local\Android\Sdk\emulator\emulator.exe"
            subprocess.Popen(f'"{emulator_path}" -avd {avd_name}', shell=True)
            time.sleep(10)

        # Wait until boot complete
        boot_completed = False
        while not boot_completed:
            check = subprocess.run("adb shell getprop sys.boot_completed", shell=True, capture_output=True, text=True)
            if "1" in check.stdout.strip():
                boot_completed = True
                print("[INFO] Emulator fully booted.")
            else:
                print("[INFO] Waiting for emulator to boot...")
                time.sleep(5)

        return True

    except Exception as e:
        log_error(f"Error starting emulator: {e}")
        return False
