import heapq
from collections import Counter


def huffman_codes(text):
    if not text:
        return {}

    frequency = Counter(text)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        char = heap[0][1][0]
        return {char: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(
            heap, [left[0] + right[0]] + left[1:] + right[1:]
        )

    return {char: code for char, code in heap[0][1:]}


def compress_text(text):
    codes = huffman_codes(text)
    encoded = "".join(codes[char] for char in text)
    return encoded, codes


def decompress_text(encoded, codes):
    reverse_codes = {code: char for char, code in codes.items()}
    result = []
    current = ""

    for bit in encoded:
        current += bit
        if current in reverse_codes:
            result.append(reverse_codes[current])
            current = ""

    return "".join(result)