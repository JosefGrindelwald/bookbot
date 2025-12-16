from stats import num_of_character
from stats import nummber_of_words
from stats import text
from stats import sort_on
count = nummber_of_words(text)
print(count)
liste = num_of_character(text)
liste.sorted(reverse=True, key = sort_on)
print(liste)
     
  
  
