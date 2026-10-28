import time


def merge_sort(arr):
    """Sort a list using Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    """Sort a list using Quick Sort."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


def compare_sorting_algorithms(arr):
    """Compare Merge Sort and Quick Sort execution times."""
    start = time.perf_counter()
    merge_result = merge_sort(arr)
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    quick_result = quick_sort(arr)
    quick_time = time.perf_counter() - start

    print("\n--- Sorting Algorithm Comparison ---")
    print("Original data:", arr)
    print("Merge Sort result:", merge_result)
    print(f"Merge Sort time: {merge_time:.8f} seconds")
    print("Quick Sort result:", quick_result)
    print(f"Quick Sort time: {quick_time:.8f} seconds")

    return merge_result, quick_result