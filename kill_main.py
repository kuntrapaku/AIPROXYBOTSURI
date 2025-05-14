import psutil

SCRIPT_NAME = "main.py"
current_pid = psutil.Process().pid

for proc in psutil.process_iter(['pid', 'cmdline']):
    try:
        cmdline = proc.info.get('cmdline') or []
        if SCRIPT_NAME in ' '.join(cmdline) and proc.pid != current_pid:
            print(f"[INFO] Killing old instance of {SCRIPT_NAME} (PID {proc.pid})")
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
