import json
import sys

import pandas as pd


def json_to_excel(json_file_path, excel_file_path):
    data = []
    with open(json_file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                json_obj = json.loads(line.strip())
                data.append(json_obj)
            except json.JSONDecodeError as e:
                print(f"Skipping malformed JSON line: {line.strip()} - Error: {e}")

    if data:
        df = pd.DataFrame(data)
        df.to_excel(excel_file_path, index=False, engine="xlsxwriter")
        print(f"Successfully converted '{json_file_path}' to '{excel_file_path}'")
    else:
        print("No valid JSON data found to convert.")


if __name__ == "__main__":
    input_json_file = sys.argv[1]
    output_excel_file = input_json_file.replace(".json", ".xlsx")
    json_to_excel(input_json_file, output_excel_file)
