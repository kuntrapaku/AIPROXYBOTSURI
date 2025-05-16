# app/main.py

from core.openai_client import get_gpt_response
from interface.cli import get_user_prompt
from interface.editor_paste import paste_to_editor
from interface.voice_input import listen_for_prompt


def run():
    mode = input("Use voice? (y/n): ").strip().lower()
    prompt = listen_for_prompt() if mode == "y" else get_user_prompt()

    print("\n🧠 Thinking...")
    response = get_gpt_response(prompt)

    print("\n📤 Response:")
    print(response)

    paste_to_editor(response)

if __name__ == "__main__":
    run()
