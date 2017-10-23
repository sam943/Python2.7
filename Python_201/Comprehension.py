# List Comprehensions
# Comprehension is an easy and natural way to generate lists and dictionaries.
"""
number = range(0,50)

# let use Comprehension List to generate only even numbers
even_numbers = [ i for i in range(0,50) if i % 2 == 0 and i>=2 ]
print even_numbers
squares = [ i*i for i in range(0,50) if i % 2 == 0 and i>=2 ]
print squares

# Strings with Compreshension List
names = ['adam' , 'Joe', 'sam', 'king','Jack', 'Jusin ' ]
names_formatted = [ x.title() for x in names ]
print names_formatted

# Find the names that start with J
names_with_j = [ name for name in names_formatted if name[0].lower() == 'j' ]
print names_with_j
"""

# Another example to encode and decode
import string
from random import shuffle
raw_text = "Hello World"
letters = list(string.ascii_letters)

encoded_letters = letters[:]
shuffle(encoded_letters)
#print encoded_letters

encoded_key = {}
decoding_key = {}
for k,v in zip(letters, encoded_letters):
	encoded_key[k]=v
	decoding_key[v]=k
#print encoded_key
encoded_text = ''
for letter in raw_text:
	encoded_text += encoded_key.get(letter,letter)

print encoded_text
encoded_text = ''.join([encoded_key.get(w,w) for w in raw_text])
decoding_text = ''.join([decoding_key.get(w,w) for w in encoded_text])
print decoding_text

# Below is another neat way of using fliping the lists using comprehension list
encoded_key = dict(zip(letters,encoded_letters))
decoding_key = dict(zip(encoded_key.values(),encoded_key.keys()))

# print the encoded value
encoded_text = ''.join([encoded_key.get(w,w) for w in raw_text])
print encoded_text
decoding_text = ''.join([decoding_key.get(w,w) for w in encoded_text])
print decoding_text
