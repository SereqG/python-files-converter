import os
from constants import POSSIBLE_EXTENSIONS

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    _, ext = os.path.splitext(file_path)
    print(f"Detected file extension: {ext}")
    return ext

def get_target_extension():
    while True:
        print("\nSelect the target extension from the list below:")
        for key, ext in POSSIBLE_EXTENSIONS.items():
            print(f"{key}: {ext}")
        try:
            choice = int(input("\nYour choice: "))
            if choice in POSSIBLE_EXTENSIONS:
                selected_ext = POSSIBLE_EXTENSIONS[choice]
                print(f"Target extension selected: {selected_ext}")
                return selected_ext
            print(f"Please enter a number between 1 and {len(POSSIBLE_EXTENSIONS)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
