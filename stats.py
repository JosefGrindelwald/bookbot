def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents 
text = get_book_text("books/frankenstein.txt")
def nummber_of_words(path_to_file):
  words = path_to_file.split()
  num_words = len(words)
  return f"Found {num_words} total words"
