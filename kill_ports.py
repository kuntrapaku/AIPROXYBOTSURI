import psutil

def kill_process_on_port(port):
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conn in proc.net_connections(kind='inet'):
                if conn.status == psutil.CONN_LISTEN and conn.laddr.port == port:
                    print(f"[INFO] Killing process {proc.pid} on port {port}")
                    proc.kill()
                    found = True
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if not found:
        print(f"[INFO] Nothing running on port {port}")

if __name__ == "__main__":
    kill_process_on_port(8080)  # Spring Boot
    kill_process_on_port(3000)  # Frontend
    kill_process_on_port(5000)  # FastAPI Agent
