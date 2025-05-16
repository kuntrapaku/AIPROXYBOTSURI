import threading
import uvicorn
import sys

from utils.monitor import monitor_services
from run_backend import run_backend
from run_frontend import run_frontend


def start_agent_server():
    """
    Starts the FastAPI server for the AI Agent.
    """
    print("[INFO] Starting AI Agent Server on port 5000...")
    uvicorn.run("agent.agent_server:app", host="0.0.0.0", port=5000, reload=False)


def main():
    print("[BOOT] Starting Backend, Frontend, AI Agent, and Monitor...")

    # ✅ Start backend and check if it built successfully
    backend_ok = run_backend()
    if not backend_ok:
        print("[FATAL] Backend failed to start or build. Continuing with agent for testing...")
        # still start agent for dev testing
    else:
        print("[OK] Backend is running on http://localhost:8080")

    # ✅ Start frontend, monitor, and agent in background threads
    frontend_thread = threading.Thread(target=run_frontend, name="FrontendThread")
    monitor_thread = threading.Thread(target=monitor_services, name="MonitorThread")
    agent_thread = threading.Thread(target=start_agent_server, name="AgentThread")

    frontend_thread.start()
    monitor_thread.start()
    agent_thread.start()

    # ✅ Wait for all threads to finish (or CTRL+C)
    try:
        frontend_thread.join()
        monitor_thread.join()
        agent_thread.join()
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] CTRL+C received. Exiting all services.")
        sys.exit(0)


if __name__ == "__main__":
    main()
