import os
from HashTable import Table


def main():
    try:
        ht = Table(capacity=19)
        with open("rfc791.txt", "r") as f:
            for line in f:
                for char in line:
                    if not char.isalpha():
                        continue
                    char = char.lower()  # optional: count a/A together
                    current_count = ht.search(char)
                    if current_count is None:
                        ht.insert(char, 1)
                    else:
                        ht.insert(char, current_count + 1)

        ht.printValues()

    except IOError as e:
        print(f"Failed to open or write to rfc919.txt: {e}")
        # You can add more specific error handling here based on 'e'
        # For example, checking for permission errors:
        if not os.access("rfc919.txt", os.W_OK):
            print("Permission denied to write to rfc919.txt")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # This block will always execute, regardless of whether an exception occurred
        print("File operation attempt completed.")


if __name__ == "__main__":
    main()
