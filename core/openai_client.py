# core/openai_client.py

from openai import OpenAI
from infrastructure.config import OPENAI_API_KEY, MODEL


client = OpenAI(api_key=OPENAI_API_KEY)

def get_gpt_response(prompt: str, model: str = MODEL) -> str:
    try:
        if not model:
            model = "gpt-3.5-turbo"

        messages = [
            {
                "role": "system",
                "content": (
            "You are ChatGPT, a large language model trained by OpenAI. "
            "Answer the user query as directly, factually, and thoroughly as possible. "
            "Do NOT say hello. Do NOT greet. Just give the user the answer."
        )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        print("\n[DEBUG] --- SENDING TO GPT ---")
        print(f"Model: {model}")
        for msg in messages:
            print(f"{msg['role']}: {msg['content']}")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        


        reply = response.choices[0].message.content
        print(f"[DEBUG] --- GPT RESPONSE ---\n{reply}\n")
        print("[DEBUG] Full raw response:", response)
        print("[DEBUG] Full raw response:", response.model_dump_json(indent=2))
        return reply

    except Exception as e:
        print(f"[OpenAI Error] {e}")
        return f"[ERROR] {e}"
