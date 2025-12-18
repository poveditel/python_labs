from src.lib.text import normalize, count_freq, top_n, tokenize

print()

print("ПрИвЕт/nМИр/t → ", normalize("ПрИвЕт\nМИр\t"))
print("ёжик, Ёлка (yo2e=True) →", normalize("ёжик, Ёлка", yo2e=True))
print("Hello\r\nWorld  →", normalize("Hello\r\nWorld"))
print("  двойные   пробелы  → ", normalize("  двойные   пробелы  "))

print()
print()

print("привет мир → ", tokenize("привет мир"))
print("hello,world!!! → ", tokenize("hello,world!!!"))
print("по-настоящему круто → ", tokenize("по-настоящему круто"))
print("2007 год → ", tokenize("2007 год"))
print("emoji 😀 не слово → ", tokenize("emoji 😀 не слово"))

print()
print()

print(
    'count_freq(["a","b","a","c","b","a","a","c","b","a","a","c","b","a"]) → ',
    count_freq(["a", "b", "a", "c", "b", "a", "a", "c", "b", "a", "a", "c", "b", "a"]),
)
print()
print(
    "top_n(..., n=2) → ",
    top_n(
        count_freq(
            ["a", "b", "a", "c", "b", "a", "a", "c", "b", "a", "a", "c", "b", "a"]
        )
    ),
)
print()
print(
    'top_n(..., n=4) ["bb","aa","bb","aa","cc", "bb","aa","cc", "bb","aa","cc"]→ ',
    top_n(
        count_freq(["bb", "aa", "bb", "aa", "cc", "bb", "aa", "cc", "bb", "aa", "cc"]),
        n=4,
    ),
)

print()
print()
