def linear_search(arr, target):
    """Find an element using Linear Search."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Find an element using Binary Search.

    The input list must already be sorted.
    Returns the index if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def compare_search_algorithms(arr, target):
    """Compare Linear Search and Binary Search."""
    sorted_arr = sorted(arr)

    linear_result = linear_search(arr, target)
    binary_result = binary_search(sorted_arr, target)

    print("\n--- Search Results ---")
    print("Original list:", arr)
    print("Sorted list for Binary Search:", sorted_arr)
    print("Target:", target)

    if linear_result != -1:
        print("Linear Search: Found at index", linear_result)
    else:
        print("Linear Search: Not found")

    if binary_result != -1:
        print("Binary Search: Found at sorted index", binary_result)
    else:
        print("Binary Search: Not found")