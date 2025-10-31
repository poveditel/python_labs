from collections import Counter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from lab03.text import normalize, tokenize
from lab04.io_txt_csv import read_text, write_csv

def main():
    input_file = "data/lab04/input.txt"
    output_file = "data/lab04/report.csv"
    
    try:
        text = read_text(input_file)
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        return
    
    normal_text = normalize(text)
    words = tokenize(normal_text)
    
    word_count = Counter(words)
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    rows = [(word, count) for word, count in sorted_words]
    write_csv(rows, output_file, header=("word", "count"))
    
    total_words = len(words)
    unique_words = len(word_count)
    top_5 = sorted_words[:5]
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
