from sorting import merge_sort
from searching import linear_search, binary_search
from compression import compress_text, decompress_text
from optimization import knapsack_01, fractional_knapsack
from Advanced_algorithm import (
    longest_common_subsequence,
    activity_selection,
    max_min
)


def run_tests():
    print("=== Algorithm Test Cases ===")

    # Test 1: Merge Sort
    result = merge_sort([5, 2, 8, 1, 3])
    print("Test 1 - Merge Sort:", result)
    assert result == [1, 2, 3, 5, 8]

    # Test 2: Linear Search
    result = linear_search(["a.txt", "b.txt"], "b.txt")
    print("Test 2 - Linear Search:", result)
    assert result == 1

    # Test 3: Binary Search (sorted filenames)
    result = binary_search(["a.txt", "b.txt", "c.txt"], "c.txt")
    print("Test 3 - Binary Search:", result)
    assert result == 2

    # Test 4: Huffman compression and decompression
    text = "aaabbc"
    encoded, codes = compress_text(text)
    decoded = decompress_text(encoded, codes)
    print("Test 4 - Huffman round trip:", decoded)
    assert decoded == text

    # Test 5: 0/1 Knapsack
    result = knapsack_01([1, 2, 3], [6, 10, 12], 5)
    print("Test 5 - 0/1 Knapsack:", result)
    assert result == 22

    # Test 6: Fractional Knapsack
    result = fractional_knapsack([10, 20, 30], [60, 100, 120], 50)
    print("Test 6 - Fractional Knapsack:", result)
    assert abs(result - 240.0) < 1e-9

    # Test 7: Longest Common Subsequence
    result = longest_common_subsequence("ABCBDAB", "BDCAB")
    print("Test 7 - LCS length:", result)
    assert result == 4

    # Test 8: Activity Selection
    result = activity_selection([(1, 3), (2, 4), (3, 5), (5, 7)])
    print("Test 8 - Activity Selection:", result)
    assert len(result) == 3

    # Test 9: Max-Min
    result = max_min([7, 2, 9, 4])
    print("Test 9 - Max-Min:", result)
    assert result == (2, 9)

    print("\nAll 9 tests passed!")


if __name__ == "__main__":
    run_tests()