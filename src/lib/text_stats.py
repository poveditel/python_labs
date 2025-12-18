import sys
from src.lib.table import print_summary


def main():
    IS_TABLE = True
    print_summary(text=sys.stdin.read(), is_table=IS_TABLE)


main()

"""
echo "Привет, мир! Привет!!!" | python -m src.lab_03.text_stats
"""
