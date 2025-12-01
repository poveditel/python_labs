from openpyxl import Workbook
import csv
import os

def csv_to_xlsx(csv_path, xlsx_path):
    workbook = Workbook()
    sheet = workbook.active

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            sheet.append(row)

    for column_cells in sheet.columns:
        max_length = 0
        column = column_cells[0].column_letter
        for cell in column_cells:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except TypeError:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width

    workbook.save(xlsx_path)