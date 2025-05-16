# interface/api/write_routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from core.file_writer import write_code_to_file

router = APIRouter()

class FileWriteRequest(BaseModel):
    filename: str  # e.g., "utils/helpers.py"
    code: str      # The actual code to write

@router.post("/write")
def write_file(request: FileWriteRequest):
    try:
        path = write_code_to_file(request.filename, request.code)
        return {"message": "✅ File created", "path": path}
    except Exception as e:
        return {"error": str(e)}
