def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()


def number_of_words(text):
    return len(text.split())


def num_of_character(text):
    characters = {}

    for c in text.lower():
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1

    return characters


def sort_characters(char_dict):
    liste = [
        {"key": k, "value": v}
        for k, v in char_dict.items()
    ]
    liste.sort(key=lambda x: x["value"], reverse=True)
    return liste



