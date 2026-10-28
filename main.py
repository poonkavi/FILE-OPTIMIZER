import os

from file_manager import scan_files
from sorting import merge_sort, quick_sort, compare_sorting_algorithms
from searching import (
    linear_search,
    binary_search,
    compare_search_algorithms
)
from compression import compress_text, decompress_text


def display_files(files):
    print("\n--- Available Files ---")
    if not files:
        print("No files found.")
        return

    for filename, size in files:
        print(f"{filename} - {size} bytes")


def sort_files(files):
    if not files:
        print("No files to sort.")
        return

    sizes = [size for filename, size in files]

    print("\n1. Merge Sort")
    print("2. Quick Sort")
    print("3. Compare both")

    choice = input("Choose sorting algorithm: ").strip()

    if choice == "1":
        print("Merge Sort result:", merge_sort(sizes))
    elif choice == "2":
        print("Quick Sort result:", quick_sort(sizes))
    elif choice == "3":
        compare_sorting_algorithms(sizes)
    else:
        print("Invalid choice.")
        return

    print("\nFiles sorted by size:")
    for filename, size in sorted(files, key=lambda item: item[1]):
        print(f"{filename} - {size} bytes")


def search_file(files):
    if not files:
        print("No files available.")
        return

    filenames = sorted(filename for filename, size in files)
    target = input("Enter filename to search: ").strip()

    print("\n1. Linear Search")
    print("2. Binary Search")
    print("3. Compare both")

    choice = input("Choose search algorithm: ").strip()

    if choice == "1":
        index = linear_search(filenames, target)
        print("Linear Search:", "Found" if index != -1 else "Not found")

    elif choice == "2":
        index = binary_search(filenames, target)
        print("Binary Search:", "Found" if index != -1 else "Not found")

    elif choice == "3":
        compare_search_algorithms(filenames, target)

    else:
        print("Invalid choice.")
        return

    if choice in ("1", "2") and index != -1:
        print("Filename:", filenames[index])


def compress_file(folder_path):
    filename = input("Enter text filename to compress: ").strip()
    path = os.path.join(folder_path, filename)

    if not os.path.isfile(path):
        print("File not found.")
        return

    try:
        with open(path, "r", encoding="utf-8") as file:
            original = file.read()

        if not original:
            print("The file is empty.")
            return

        encoded, codes = compress_text(original)

        with open(path + ".huff", "w", encoding="utf-8") as file:
            file.write(encoded)

        with open(path + ".codes.txt", "w", encoding="utf-8") as file:
            for char, code in codes.items():
                file.write(f"{ord(char)}:{code}\n")

        original_size = len(original.encode("utf-8"))

        print("Compression encoding completed.")
        print("Encoded data:", path + ".huff")
        print("Code table:", path + ".codes.txt")
        print("Original size:", original_size, "bytes")
        print("Encoded length:", len(encoded), "bits")
        print("Note: This demonstration stores encoded bits as text.")

    except (OSError, UnicodeError, ValueError) as error:
        print("Compression error:", error)


def decompress_file(folder_path):
    filename = input(
        "Enter original filename (for example, notes.txt): "
    ).strip()
    path = os.path.join(folder_path, filename)

    try:
        with open(path + ".huff", "r", encoding="utf-8") as file:
            encoded = file.read()

        codes = {}
        with open(path + ".codes.txt", "r", encoding="utf-8") as file:
            for line in file:
                char_code, bit_code = line.rstrip("\n").split(":", 1)
                codes[chr(int(char_code))] = bit_code

        restored = decompress_text(encoded, codes)
        output_path = path + ".restored.txt"

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(restored)

        with open(path, "r", encoding="utf-8") as file:
            original = file.read()

        print("Decompression completed.")
        print("Restored file:", output_path)
        print("Content matches original:", restored == original)

    except (OSError, UnicodeError, ValueError) as error:
        print("Decompression error:", error)


def main():
    folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sample_files"
    )
    os.makedirs(folder_path, exist_ok=True)

    print("\n=== FILE COMPRESSION AND DATA ORGANIZATION SYSTEM ===")

    while True:
        files = scan_files(folder_path)

        print("\n1. Display files")
        print("2. Sorting algorithms")
        print("3. Search for a file")
        print("4. Compress a text file")
        print("5. Decompress a text file")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_files(files)
        elif choice == "2":
            sort_files(files)
        elif choice == "3":
            search_file(files)
        elif choice == "4":
            compress_file(folder_path)
        elif choice == "5":
            decompress_file(folder_path)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1-6.")


if __name__ == "__main__":
    main()