import sys
from stats import (
    get_book_text,
    number_of_words,
    num_of_character,
    sort_characters
)

# 🔹 Argument prüfen
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")

text = get_book_text(path)

print("----------- Word Count ----------")
print(f"Found {number_of_words(text)} total words")

print("--------- Character Count -------")

characters = num_of_character(text)
sorted_chars = sort_characters(characters)

for d in sorted_chars:
    print(f"{d['key']}: {d['value']}")

print("============= END ===============")
  
