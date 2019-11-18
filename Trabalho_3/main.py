from huffman import *

text = 'EDUARDOTONATTO'

print("\nFrequency:")
frequency = frequency(text)
print(frequency)

print("\nPrefixes:")
prefixes = prefix(frequency)
print(prefixes)

print("\nDictionary:")
dictionary = dictionary(prefixes)
print(dictionary)

print("\nEncrypted Text:")
encrypted_text = encrypt(text, dictionary)
print(encrypted_text)

print("\nDecrypted Text:")
decrypted_text = decrypt_text(encrypted_text, prefixes)
print(decrypted_text)

print("\nCompressed Text:")
compressed_text = compress(encrypted_text)
print(compressed_text)

print("\nUnpacked Text:")
unpacked_text = unpack(compressed_text, prefixes)
print(unpacked_text)
