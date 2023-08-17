import uuid


def generatehexstring(length: int) -> str:
    length = length if 0 <= length <= 36 else 36
    string = str(uuid.uuid4())[:length-1] + 'A'
    return string



