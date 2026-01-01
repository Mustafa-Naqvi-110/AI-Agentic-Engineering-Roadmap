import json

def parse_json_safely(text: str) -> dict:
    """
    Converts a JSON string into a Python dictionary.
    Raises a clear error if JSON is invalid.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON returned:\n{text}")
