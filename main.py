from stats import num_of_character
from stats import nummber_of_words
from stats import text
from stats import liste
from stats import sort_on
count = nummber_of_words(text)
print(count)
liste.sort(key=sort_on, reverse=True)
for d in liste:
    print(f"{*d.values()}:)
     
  
  
