# core/openai_client.py

from openai import OpenAI
from infrastructure.config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def get_gpt_response(prompt: str, model: str = MODEL) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[OpenAI Error] {e}")
        return "Error: Unable to fetch response from OpenAI"
