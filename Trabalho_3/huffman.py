from collections import Counter
import heapq

LEFT = 2
RIGHT = 3

def frequency(text):
    return Counter(text)

def join_node(left, right):
    frequency = left[0] + right[0]
    parent = (frequency, '', left, right)
    return parent

def prefix(frequency):
    tree = []
    for char, freq in frequency.items():
        heapq.heappush(tree, (freq, char))

    print(tree)

    while len(tree) > 1:
        left = heapq.heappop(tree)
        right = heapq.heappop(tree)
        parent = join_node(left, right)
        heapq.heappush(tree, parent)
    root = tree[0]
    return root

def dictionary(tree, symbol = ''):
    node = tree[1]

    if node is not '':
        return {node: symbol or '0'}
    else:
        left_branch = dictionary(tree[LEFT], symbol + '0')
        right_branch = dictionary(tree[RIGHT], symbol + '1')
        left_branch.update(right_branch)
        return left_branch

def encrypt(text, dictionary):
    return "".join([dictionary[letter] for letter in text])

def decrypt_text(codes, tree):
    text = []
    node = tree
    for code in codes:
        if node[1] is '':
            if code == '0':
                node = node[LEFT]
            elif code == '1':
                node = node[RIGHT]
        if node[1] is not '':
            text.append(node[1])
            node = tree
    return "".join(text)

def compress(codes):
    bytes = [chr(int(codes[i:i+8], 2)) for i in range(0, len(codes), 8)]
    return "".join(bytes)

def unpack(compressed_text, prefix):
    bytes = [bin(ord(byte))[2:] for byte in compressed_text]
    for i in range(0, len(bytes) - 1):
        bytes[i] = bytes[i].zfill(8)
    compressed_text = "".join(bytes)
    unpacked_text = decrypt_text(compressed_text, prefix)
    return unpacked_text
