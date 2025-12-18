import re


def format_record(rec: tuple[str, str, float]) -> str:
    group, gpa = rec[1], rec[2]
    name = rec[0].split()
    fio = name[0].capitalize() + " " + name[1][0].upper() + "."
    if len(name) == 3:
        fio += " "
        fio += name[-1][0].upper() + "."
    return f"{fio}, гр. {group}, GPA {gpa:.2f}"


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        while "Ё" in text or "ё" in text:
            text = text.replace("ё", "е").replace("Ё", "Е")
    while "\t" in text or "\r" in text or "\n" in text:
        text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while "  " in text:
        text = text.replace(" " * 2, " ")
    return text.strip()


def tokenize(text: str) -> list[str]:
    text = text.lower()

    pattern = r"[\wа-яё]+"

    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    co = {}
    for i in tokens:
        if i in co:
            co[i] += 1
        else:
            co[i] = 1
    return co


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = sorted(freq.items(), key=lambda item: [-item[1], item[0]])
    top_n = []
    for i in range(min(n, len(freq))):
        top_n.append((freq[i][0], freq[i][1]))
    return top_n
