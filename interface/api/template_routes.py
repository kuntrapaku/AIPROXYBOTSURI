# interface/api/template_routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from core.openai_client import get_gpt_response
from core.prompt_templates import fill_template
from interface.editor_paste import paste_to_editor
from core.file_writer import write_code_to_file

router = APIRouter()

class TemplatePromptRequest(BaseModel):
    template: str  # e.g., "unit_test", "explain"
    code: str      # your raw function or snippet
    paste: bool = True
    save_as: str | None = None  # optional: filename to write to disk

@router.post("/template")
def handle_template_prompt(request: TemplatePromptRequest):
    try:
        prompt = fill_template(request.template, code=request.code)
    except ValueError as e:
        return {"error": str(e)}

    response = get_gpt_response(prompt)

    if request.paste:
        paste_to_editor(response)

    if request.save_as:
        path = write_code_to_file(request.save_as, response)
    else:
        path = None

    return {
        "template": request.template,
        "filled_prompt": prompt,
        "response": response,
        "pasted": request.paste,
        "file_saved": path
    }
