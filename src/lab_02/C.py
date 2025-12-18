from src.lib.text import format_record

print()
print()
print()

print(
    '("Иванов Иван Иванович", "BIVT-25", 4.6) -                ',
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)),
)
print(
    '("Петров Пётр", "IKBO-12", 5.00) -                        ',
    format_record(("Петров Пётр", "IKBO-12", 5.00)),
)
print(
    '("Петров Пётр Петрович", "IKBO-12", 5.0) -                ',
    format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)),
)
print(
    '("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -      ',
    format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)),
)

print()
print()
print()
