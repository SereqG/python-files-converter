import csv
import json

import constants

import pandas as pd

def json_to_csv(input_path):
    """
    Converts JSON data (list or dict) to a CSV file and writes to output_path.
    """
    output_path = f"{constants.OUTPUT_FILE_PATH}.csv"
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load JSON: {e}")
    
    df = pd.json_normalize(data)

    with open(output_path, "w", newline='') as csvfile:
        columns = df.columns.to_list()

        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        for row in df.to_dict(orient="records"):
            writer.writerow(row)
    print(f"File converted successfully: {output_path}")
