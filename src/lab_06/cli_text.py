import argparse
from pathlib import Path

from src.lib.text import count_freq, tokenize, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")

    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")

    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")

    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")

    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")

    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество наиболее частых слов"
    )

    args = parser.parse_args()

    filepath = Path(args.input)

    if not filepath.exists():
        raise FileNotFoundError(f"Файл {filepath} не найден")

    if args.command == "cat":
        with filepath.open("r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":
        content = [i for i in filepath.open("r", encoding="utf-8")]
        tokens = tokenize(text="".join(content))
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)

        num = 1
        for q, w in top:
            print(f"{num}. {q} - {w}")
            num += 1


if __name__ == "__main__":
    main()
