import threading
import uvicorn
import psutil
import sys

from utils.monitor import monitor_services
from run_backend import run_backend
from run_frontend import run_frontend


# def is_already_running(script_name="main.py"):
#     """
#     Prevents multiple instances of the orchestrator from running.
#     """
#     current_pid = psutil.Process().pid
#     for proc in psutil.process_iter(['pid', 'cmdline']):
#         try:
#             cmdline = proc.info.get('cmdline') or []
#             if script_name in ' '.join(cmdline) and proc.pid != current_pid:
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue
#     return False


def start_agent_server():
    """
    Starts the FastAPI server for the AI Agent.
    """
    uvicorn.run("agent.agent_server:app", host="0.0.0.0", port=5000, reload=False)


def main():
    print("Starting Backend, Frontend, and Monitoring Services...")

    # ✅ Prevent duplicate main.py instances
    # if is_already_running():
    #     print("[WARN] Another instance of main.py is already running. Exiting.")
    #     sys.exit(1)

    # ✅ Start backend synchronously
    backend_ok = run_backend()
    if not backend_ok:
        print("[FATAL] Backend failed to start. Aborting.")
        return

    # ✅ Start other services in threads
    frontend_thread = threading.Thread(target=run_frontend)
    monitor_thread = threading.Thread(target=monitor_services)
    agent_thread = threading.Thread(target=start_agent_server)

    frontend_thread.start()
    monitor_thread.start()
    agent_thread.start()

    # ✅ Join threads gracefully, allow CTRL+C exit
    try:
        frontend_thread.join()
        monitor_thread.join()
        agent_thread.join()
    except KeyboardInterrupt:
        print("\n[INFO] Shutdown requested. Exiting gracefully...")
        sys.exit(0)


if __name__ == "__main__":
    main()
