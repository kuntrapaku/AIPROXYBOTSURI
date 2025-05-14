import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file relative to this file's location
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# OpenAI API Key (loaded from environment variable)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Project Paths (use environment variables with fallback)
INTELLIJ_PROJECT_PATH = os.getenv("INTELLIJ_PROJECT_PATH", "C:/Users/suri2/mvc")
REACT_NATIVE_PATH = os.getenv("REACT_NATIVE_PATH", "C:/Users/suri2/mvmobapp")

# Logging Path
LOG_FILE = os.path.join(os.getcwd(), "logs", "error.log")
