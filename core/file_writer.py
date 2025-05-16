# core/file_writer.py

import os

def write_code_to_file(relative_path: str, content: str) -> str:
    """
    Creates or overwrites a file with the given content.
    Path is relative to the project root.
    Returns the full path written.
    """
    full_path = os.path.abspath(relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"✅ File written to: {full_path}")
    return full_path
