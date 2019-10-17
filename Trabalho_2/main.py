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

def print_dictionary():
    for letter in string.ascii_letters:
        print("Letra = {letter}, traduzida como {dictionary_letter}".format(letter=letter, dictionary_letter=dictionary[letter]))

def encrypt_text(text):
    encrypted_text = ""
    for letter in text:
        if letter not in string.ascii_letters:
            encrypted_text = encrypted_text + " "
        else:
            encrypted_text = encrypted_text + dictionary[letter]
    print(encrypted_text)

dictionary = shuffle_dictionary()
#print_dictionary()
text = input("Informe um texto para cifrar: ")
#print(text)
encrypt_text(text)
