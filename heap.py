import heapq
from collections import Counter
import sys

class Node(object):
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

class Huffman:
    def __init__(self, text):
        self.codes = {}
        self.heap = []
        self.text = text
        frequency = self.get_frequency()
        for char in frequency:
            heapq.heappush(self.heap, Node(char, frequency[char]))

    def get_frequency(self):
        return Counter(self.text)

    def merge_nodes(self, node1, node2):
        new_node = Node('', node1.frequency + node2.frequency)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(self.heap, new_node)

    def compose_codes(self, node, curr_code):
        if node.char:
            self.codes[node.char] = curr_code
        else:
            self.compose_codes(node.left, curr_code + '0')
            self.compose_codes(node.right, curr_code + '1')

    def get_codes(self):
        while len(self.heap) > 1:
            value1 = heapq.heappop(self.heap)
            value2 = heapq.heappop(self.heap)
            self.merge_nodes(value1, value2)
    
        root = heapq.heappop(self.heap)
        self.compose_codes(root, '')
        return self.codes


    def encode(self):
        if not self.codes:
            self.codes = self.get_codes()
        return ''.join(map(lambda ch: self.codes[ch], self.text)).encode('ascii')


    def decode(self, encoded):
        if not self.codes:
            return

        reversed_codes = dict(zip(self.codes.values(), self.codes.keys()))
        res = ''
        code = ''

        for bit in encoded:
            code += bit
            if code in self.codes.values():
                res += reversed_codes[code]
                code = ''
        return res

            
    def get_memory_improvement(self):
        text_memory = len(self.text) * 8
        encode_memory = len(self.encode())
        return (text_memory - encode_memory) / text_memory * 100
