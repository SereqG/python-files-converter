import json

from converters.json_to_xml import convert_json_to_xml
from converters.json_to_xlsx import json_to_xlsx
from converters.json_to_csv import json_to_csv

def convert_file(target_extension, input_path, input_ext, output_path):
    if input_ext == "json":
        try:
            if target_extension == ".xml":
                with open(input_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                xml_tree = convert_json_to_xml(data)
                xml_tree.write(output_path, encoding="utf-8", xml_declaration=True)
                print(f"File converted successfully: {output_path}")
                return
            elif target_extension == ".xlsx":
                json_to_xlsx(input_path)
                return
            elif target_extension == ".csv":
                json_to_csv(input_path)
                return
            else:
                print(f"Conversion from {input_ext} to {target_extension} is not supported yet.")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")
    else:
        print("You have to provide json file")