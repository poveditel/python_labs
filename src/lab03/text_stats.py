from text import normalize, tokenize, count_freq, top_n
text = input("Введите текст: ")
normalized_text = normalize(text)
tokens = tokenize(normalized_text)
freq_dict = count_freq(tokens)
top_words = top_n(freq_dict, 5)
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq_dict)}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}:{count}")