

def get_part_text(text: str) -> str:
    with open(text, 'r', encoding='utf-8') as file:
        res = file.read()
    return res