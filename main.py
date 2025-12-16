import sys
from stats import (
    get_book_text,
    number_of_words,
    num_of_character,
    sort_characters
)


if len(sys.argv) != 2:
    print("Usage: python main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]



text = get_book_text(path)

print(f"Found {number_of_words(text)} total words")



characters = num_of_character(text)
sorted_chars = sort_characters(characters)

for d in sorted_chars:
    print(f"{d['key']}: {d['value']}")

print("============= END ===============")
  
  
