import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_codes(char_freq):
    heap = []

    # Build heap
    for ch, freq in char_freq.items():
        heapq.heappush(heap, Node(freq, ch))

    # Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    # Generate codes
    def generate(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return

        generate(node.left, code + "0")
        generate(node.right, code + "1")

    generate(root, "")
    return codes


# -------- HARDCODED INPUT --------
char_freq = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}


# -------- PRINT INPUT --------
print("Input: Character Frequencies")
for ch, freq in char_freq.items():
    print(f"{ch} : {freq}")


# -------- PROCESS --------
codes = huffman_codes(char_freq)


# -------- PRINT OUTPUT --------
print("\nOutput: Huffman Codes\n")
for ch in sorted(codes):
    print(f"{ch} : {codes[ch]}")