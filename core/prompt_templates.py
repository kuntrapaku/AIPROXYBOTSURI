# core/prompt_templates.py

TEMPLATES = {
    "unit_test": "Write a unit test for the following function:\n{code}",
    "explain": "Explain what this code does:\n{code}",
    "optimize": "Optimize the following code for performance:\n{code}",
    "convert_to_java": "Convert this Python code to Java:\n{code}"
}

def fill_template(name: str, **kwargs) -> str:
    """
    Fills a template with provided variables.
    Example: fill_template("unit_test", code=some_code)
    """
    template = TEMPLATES.get(name)
    if not template:
        raise ValueError(f"Template '{name}' not found.")
    return template.format(**kwargs)
