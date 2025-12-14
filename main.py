def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents 
text = get_book_text("books/frankenstein.txt")
def nummber_of_words(path_to_file):
  num_words = 0
  words = path_to_file.split()
  for i in range(0, len(words), 1):
    num_words += 1
    return f"Found {num_words} total words"
count = nummber_of_words("books/frankenstein.txt")
print(count)
  
  
