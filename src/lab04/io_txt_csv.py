from pathlib import Path
import csv

def read_text(path, encoding="utf-8"):
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)

def write_csv(rows, path, header=None):
    file_path = Path(path)
    rows_list = list(rows)
    
    if rows_list:
        first_row_length = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_row_length:
                raise ValueError(f"Строка {i} имеет другую длину")
    
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        if header is not None:
            writer.writerow(header)
        
        for row in rows_list:
            writer.writerow(row)

def ensure_parent_dir(path):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)