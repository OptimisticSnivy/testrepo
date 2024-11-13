import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    # Create a priority queue with initial nodes
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(root):
    codes = {}

    def encode(node, code):
        if node:
            if node.char is not None:
                codes[node.char] = code
            encode(node.left, code + "0")
            encode(node.right, code + "1")

    encode(root, "")
    return codes


# Example usage
frequencies = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}

# Build the Huffman tree and generate codes
root = build_huffman_tree(frequencies)
huffman_codes = generate_huffman_codes(root)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
