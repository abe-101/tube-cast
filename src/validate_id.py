import re


def valid_id(id: str) -> bool:
    match = re.match(r"[a-zA-Z0-9_-]{11}", id)
    if match:
        return True
    else:
        return False
