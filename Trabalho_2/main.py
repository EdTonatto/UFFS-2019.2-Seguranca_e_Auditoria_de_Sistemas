import string
from collections import OrderedDict
from random import shuffle

def shuffle_dictionary():
    dictionary = {}
    for letter in string.ascii_letters:
        dictionary[letter] = letter
    keys = list(dictionary.keys())
    shuffle(keys)
    return dict(OrderedDict(zip(keys, dictionary.values())))

dictionary = shuffle_dictionary()
print(dictionary)
