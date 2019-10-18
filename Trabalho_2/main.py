import string
from collections import OrderedDict
from random import shuffle

histogram_dict = {}
encrypt_dict = {}

def shuffle_dictionary():
    for letter in string.ascii_letters:
        encrypt_dict[letter] = letter
    keys = list(encrypt_dict.keys())
    shuffle(keys)
    return dict(OrderedDict(zip(keys, encrypt_dict.values())))

def print_encrypt_dict():
    for letter in string.ascii_letters:
        print("Letra = {letter}, traduzida como {dictionary_letter}".format(letter=letter, dictionary_letter=encrypt_dict[letter]))

def encrypt_text(text):
    encrypted_text = ""
    for letter in text:
        if letter not in string.ascii_letters:
            encrypted_text = encrypted_text + " "
        else:
            encrypted_text = encrypted_text + encrypt_dict[letter]
    print(encrypted_text)

def print_histogram_dict():
    for letter in string.ascii_letters:
        print("A letra {letter} apareceu {times} na lista de palavras.".format(letter=letter, times=histogram_dict[letter]))

def create_histogram():
    for letter in string.ascii_letters:
        histogram_dict[letter] = 0
    with open("word_list", 'r') as wlist:
        for word in wlist:
            for wletter in word:
                if wletter in string.ascii_letters:
                    histogram_dict[wletter] = histogram_dict[wletter] + 1

encrypt_dict = shuffle_dictionary()
print_encrypt_dict()
#text = input("Informe um texto para cifrar: ")
#print(text)
#encrypt_text(text)
create_histogram()
print_histogram_dict()
