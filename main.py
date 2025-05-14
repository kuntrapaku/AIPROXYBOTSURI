import threading
from utils.monitor import monitor_services
from run_backend import run_backend
from run_frontend import run_frontend
from threading import Thread
import uvicorn


def start_agent_server():
    """
    Starts the FastAPI server for the AI Agent.
    This exposes a POST /ask endpoint on port 5000.
    """
    # Binding to 0.0.0.0 is important so mobile app (React Native) can access it over LAN
    uvicorn.run("agent.agent_server:app", host="0.0.0.0", port=5000, reload=False)



def main():
    print("Starting Backend, Frontend, and Monitoring Services...")

    # ✅ Run backend synchronously and wait
    backend_ok = run_backend()
    if not backend_ok:
        print("[FATAL] Backend failed to start. Aborting.")
        return

    # ✅ Run frontend
    frontend_thread = threading.Thread(target=run_frontend)
    frontend_thread.start()

    # ✅ Monitor only after frontend starts
    monitor_thread = threading.Thread(target=monitor_services)
    monitor_thread.start()

    agent_thread = threading.Thread(target=start_agent_server)
    agent_thread.start()

    frontend_thread.join()
    monitor_thread.join()
    agent_thread.join()
    



if __name__ == "__main__":
    main()
