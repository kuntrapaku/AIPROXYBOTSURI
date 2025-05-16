# interface/api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from core.openai_client import get_gpt_response
from interface.editor_paste import paste_to_editor

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    paste: bool = True  # Optional: whether to paste into editor

@router.post("/prompt")
def handle_prompt(request: PromptRequest):
    prompt = request.prompt.strip()
    response = get_gpt_response(prompt)

    if request.paste:
        paste_to_editor(response)

    return {
        "prompt": prompt,
        "response": response
    }
