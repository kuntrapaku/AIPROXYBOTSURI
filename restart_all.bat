@echo off
echo [CLEANUP] Closing ports...
call env\Scripts\activate.bat

python kill_ports.py
python kill_main.py

echo [START] Launching orchestrator...
start "" python main.py

echo [OK] Orchestrator launched. You can now close this window.
pause >nul
