import os
from HashTable import Table


def main():
    user_path = input("Please enter the full path to the file \n")

    if os.path.exists(user_path):
        if not os.path.isfile(user_path):
            print("The path is not a file")
            return
    else:
        print(f"The path '{user_path}' does not exist.")
        return

    try:
        ht = Table(capacity=19)
        with open(user_path, "r") as f:
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
        print(f"Failed to open or write: {e}")
        # You can add more specific error handling here based on 'e'
        # For example, checking for permission errors:
        if not os.access("rfc919.txt", os.W_OK):
            print("Permission denied to write")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # This block will always execute, regardless of whether an exception occurred
        print("File operation attempt completed.")


if __name__ == "__main__":
    main()
