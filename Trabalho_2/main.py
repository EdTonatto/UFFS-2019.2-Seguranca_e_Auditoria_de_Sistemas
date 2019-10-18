import string
import wikipedia
from collections import OrderedDict
from random import shuffle

histogram_dict_wl = {}
histogram_dict_w = {}
encrypt_dict = {}
text = ""

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
    return encrypted_text

def print_histogram_dict():
    print("\nMostrando histograma ordenado alfabeticamente:")
    for letter in string.ascii_letters:
        print("A letra {letter} apareceu {times} na lista de palavras.".format(letter=letter, times=histogram_dict_wl[letter]))

def print_ordered_histogram_dict():
    keys = list(histogram_dict_wl.keys())
    print("\nMostrando histograma ordenado por aparicoes:")
    for key in keys:
        print("-> A letra {letter} apareceu {times} na lista de palavra".format(letter=key, times=histogram_dict_wl[key]))

def order_histogram_wl():
    return dict(OrderedDict(sorted(histogram_dict_wl.items(), key=lambda x: x[1], reverse=True)))

def create_histogram_wl():
    for letter in string.ascii_letters:
        histogram_dict_wl[letter] = 0
    with open("word_list", 'r') as wlist:
        for word in wlist:
            for wletter in word:
                if wletter in string.ascii_letters:
                    histogram_dict_wl[wletter] = histogram_dict_wl[wletter] + 1

def order_histogram_w():
    return dict(OrderedDict(sorted(histogram_dict_w.items(), key=lambda x: x[1], reverse=True)))

def create_histogram_w():
    for letter in string.ascii_letters:
        histogram_dict_w[letter] = 0
    for wletter in text:
        if wletter in string.ascii_letters:
            histogram_dict_w[wletter] = histogram_dict_w[wletter] + 1

encrypt_dict = shuffle_dictionary()
#print_encrypt_dict()

text = wikipedia.page("United States").content
#text = encrypt_text(input("Informe um texto para cifrar: "))
print(text)

create_histogram_wl()
histogram_dict_wl = order_histogram_wl()
#print_histogram_dict()
#print_ordered_histogram_dict()

create_histogram_w()
histogram_dict_w = order_histogram_w()

print(histogram_dict_wl)
print(histogram_dict_w)
