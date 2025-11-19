# src/lab03/text_stats.py
import sys
import os

# Добавляем путь к модулю
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text import normalize, tokenize, count_freq, top_n

def main():
    # Читаем весь ввод из stdin
    text = sys.stdin.read()
    
    # Проверяем что текст не пустой
    if not text.strip():
        print("Ошибка: Входной текст пуст")
        return
    
    # Обрабатываем текст
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, 5)
    
    # Выводим статистику
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
    