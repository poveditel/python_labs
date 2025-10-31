import csv
from pathlib import Path

def read_text(path, encoding="utf-8"):
    """Читает файл и возвращает текст"""
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)

def write_csv(rows, path, header=None):
    """Записывает данные в CSV файл"""
    file_path = Path(path)
    
    # Проверяем что все строки одинаковой длины
    if rows:
        first_length = len(rows[0])
        for row in rows:
            if len(row) != first_length:
                raise ValueError("Все строки должны быть одинаковой длины")
    
    # Создаем папки если нужно
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Записываем файл
    with file_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)