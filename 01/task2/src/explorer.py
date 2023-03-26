"""Generator for lines with keywords from file."""

def search_lines(words: list, file) -> str:
    """Генератор для поиска строк, содержащих слова из списка words"""
    if isinstance(file, str):
        file = open(file, "r", encoding="utf-8")
    with file:
        while (line := file.readline().rstrip('\n')):
            for word in words:
                if word.lower() in line.lower().split(" "):
                    yield line
                    break
