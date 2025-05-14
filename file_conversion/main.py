import os

from utils.file_handler import process_file, get_target_extension
from utils.convert_file import convert_file

import constants

def main() -> None:
    input_path = input("Pass input file path: ").strip()

    if not os.path.isfile(input_path):
        print("File not found")
        return 

    input_ext = process_file(input_path)
    if not input_ext:
        return

    target_ext = get_target_extension()
    output_path = f"{constants.OUTPUT_FILE_PATH}{target_ext}"
    convert_file(target_ext, input_path, input_ext, output_path)


if __name__ == "__main__":
    print("Error: Unsupported or unreadable input file.")
    main()
