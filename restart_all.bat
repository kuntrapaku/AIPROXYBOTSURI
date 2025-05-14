@echo off
echo Killing Java, Node, ADB...
taskkill /F /IM java.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM adb.exe >nul 2>&1

echo Starting services fresh...
cd /d C:\Users\suri2\AI\ai-proxy-bot
call env\Scripts\activate
python main.py
