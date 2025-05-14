import os
from typing import Optional

from constants import POSSIBLE_EXTENSIONS

def process_file(file_path: str) -> Optional[str]:
    """
    Checks if a file exists and returns its extension (without dot) if valid.
    """
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None
    _, ext = os.path.splitext(file_path)
    ext = ext.lower().lstrip(".")
    print(f"Detected file extension: {ext}")
    return ext

def get_target_extension() -> str:
    """
    Prompts the user to select a target extension from predefined options.
    """
    while True:
        print("\nSelect the target extension from the list below:")
        for key, ext in POSSIBLE_EXTENSIONS.items():
            print(f"{key}: {ext}")
        try:
            choice = int(input("\nYour choice: ").strip())
            if choice in POSSIBLE_EXTENSIONS:
                selected_ext = POSSIBLE_EXTENSIONS[choice]
                print(f"Target extension selected: {selected_ext}")
                return selected_ext
            print(f"Please enter a number between 1 and {len(POSSIBLE_EXTENSIONS)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
