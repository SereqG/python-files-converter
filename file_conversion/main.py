from utils.file_handler import process_file, get_target_extension
from converters.json_to_xml import convert_json_to_xml
from converters.json_to_xlsx import json_to_xlsx

import json
import constants

def convert_file(target_extension, input_path, input_ext, output_path):
    try:
        if input_ext == ".json" and target_extension == ".xml":
            with open(input_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            xml_tree = convert_json_to_xml(data)
            xml_tree.write(output_path, encoding="utf-8", xml_declaration=True)
            print(f"File converted successfully: {output_path}")
        if input_ext == ".json" and target_extension == ".xlsx":
            json_to_xlsx(input_path)
        else:
            print(f"Conversion from {input_ext} to {target_extension} is not supported yet.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")


def main():
    input_path = "files/input/test.json"

    input_ext = process_file(input_path)
    if not input_ext:
        return

    target_ext = get_target_extension()
    output_path = f"{constants.OUTPUT_FILE_PATH}{target_ext}"
    convert_file(target_ext, input_path, input_ext, output_path)


if __name__ == "__main__":
    main()
