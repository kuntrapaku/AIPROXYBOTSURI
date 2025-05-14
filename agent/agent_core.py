# agent/agent_core.py

"""
This is the core AI logic module.
It handles communication with the OpenAI API and returns intelligent responses.
"""

import os
import openai
from dotenv import load_dotenv


load_dotenv()

# ✅ Set your OpenAI API key (you can also load this from env)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure it's set in your environment

def ask_agent(prompt: str) -> str:
    """
    Sends a prompt to OpenAI and returns the response.

    Args:
        prompt (str): User input

    Returns:
        str: LLM response
    """
    try:
        # Use GPT-4 or fallback to GPT-3.5
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can change to "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are an intelligent AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"[ERROR] Failed to get response from OpenAI: {e}"
