def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents 
text = get_book_text("books/frankenstein.txt")
def nummber_of_words(path_to_file):
  words = path_to_file.split()
  num_words = len(words)
  return f"Found {num_words} total words"
def num_of_character(path_to_file):
  characters = {}
  for i in path_to_file.lower():
    if i.isalpha():
      if i in characters:
        characters[i]+= 1
      else:
        characters[i] = 1
  return characters 
def sort_on(char):
  return char["num"]
    


