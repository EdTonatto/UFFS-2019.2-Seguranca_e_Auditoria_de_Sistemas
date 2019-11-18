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
