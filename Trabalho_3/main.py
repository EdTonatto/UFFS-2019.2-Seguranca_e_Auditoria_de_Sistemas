from huffman import *

text = 'EDUARDOTONATTO'

frequency = frequency(text)
print(frequency)

prefix = prefix(frequency)
print(prefix)

dictionary = dictionary(prefix)
print(dictionary)

encrypted_text = encrypt(text, dictionary)
print(encrypted_text) 
