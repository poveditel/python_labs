def format_record(rec):
    fio, group, gpa = rec
    if not fio or not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group or not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    fio_clean = ' '.join(fio.split())  # минус лишние пробелы
    fio_clean = fio_clean.title()      # первые буквы заглавнык
    parts = fio_clean.split()
    surname = parts[0] 
    initials = []
    for name in parts[1:]:  
        if name:  
            initials.append(name[0] + '.')  
    if initials:
        formatted_fio = surname + ' ' + ''.join(initials)
    else:
        formatted_fio = surname
    formatted_gpa = f"{gpa:.2f}"
    result = f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"
    return result
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Петр", "IKBO-12", 5.0)))
print(format_record(("Петров Петр Петрович", "IKBO-12", 5.0)))
print(format_record((" сидорова айна сергеевна ", "ABB-01", 3.999)))
print(format_record(("  ", "", )))
