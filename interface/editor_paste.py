# interface/editor_paste.py

import pyperclip
import pyautogui
import time
import platform

def paste_to_editor(text: str, wait_seconds: int = 2):
    """
    Copies text to clipboard and pastes into the currently active editor window.
    Works with VS Code, IntelliJ, Notepad++, etc.
    """
    pyperclip.copy(text)
    print("📋 Copied to clipboard. Click into your editor (e.g., VS Code)...")

    time.sleep(wait_seconds)  # Give time to switch focus

    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")  # macOS
    else:
        pyautogui.hotkey("ctrl", "v")     # Windows/Linux

    print("✅ Pasted into active window.")
