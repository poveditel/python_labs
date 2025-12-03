from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv, ensure_parent_dir

def create_report(input_file="data/input.txt", output_file="data/report.csv", encoding="utf-8"):
    try:
        text = read_text(input_file, encoding)
    except FileNotFoundError:
        print(f"ОШИБКА: Файл {input_file} не найден!")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"ОШИБКА: Не удалось прочитать файл в кодировке {encoding}!")
        sys.exit(1)
    
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")
    
    sorted_words = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    csv_data = []
    for word, count in sorted_words:
        csv_data.append([word, count])
    
    ensure_parent_dir(output_file)
    write_csv(csv_data, output_file, header=("word", "count"))
    print(f"Отчет сохранен в: {output_file}")

if __name__ == "__main__":
    create_report()


