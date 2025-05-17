from core.openai_client import get_gpt_response

def ask_agent(prompt: str) -> str:
    return get_gpt_response(prompt)
