from openpyxl import Workbook
import pandas as pd

import json
import constants

def json_to_xlsx(input_path):
    """
    Converts JSON data (list or dict) to an XLSX file and saves it to output_path.
    """
    output_path = f"{constants.OUTPUT_FILE_PATH}.xlsx"
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load JSON: {e}")

    df = pd.json_normalize(data)

    wb = Workbook()
    ws = wb.active

    ws.append(df.columns.tolist())

    for _, row in df.iterrows():
        ws.append(row.tolist())

    wb.save(output_path)
    print(f"File converted successfully: {output_path}")

    
    