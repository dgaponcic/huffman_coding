import heapq
from heap import Node, Huffman



def main():
  huffman = Huffman('huffman is cool')
  print(huffman.get_memory_improvement())
  print(huffman.decode('01101111101101010011000111001000010100111011001001110'))
main()
