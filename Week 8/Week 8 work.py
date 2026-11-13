from random import *
characters = ["rob", "bob", "mob", "dob", "pob"]
shuffle(characters)
sent = characters[0]
for char in characters[1:len(characters) - 1]: sent += f', {char}'
sent += f' and {characters[-1]}.'
print(sent)
