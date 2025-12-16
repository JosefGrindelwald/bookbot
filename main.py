from stats import num_of_character
from stats import nummber_of_words
from stats import text
from stats import liste
from stats import sort_on
print("============ BOOKBOT ============
      Analyzing book found at books/frankenstein.txt...
      ----------- Word Count ----------")
count = nummber_of_words(text)
print(count)
print("--------- Character Count -------")
liste.sort(key=sort_on, reverse=True)
for d in liste:
    print(": ".join(map(str, d.values())))
     
  
  
