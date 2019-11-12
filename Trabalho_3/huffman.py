from collections import Counter
import heapq

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
