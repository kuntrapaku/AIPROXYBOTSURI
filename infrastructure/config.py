# infrastructure/config.py

from dotenv import load_dotenv
import os

# Load from .env file in the root directory
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
