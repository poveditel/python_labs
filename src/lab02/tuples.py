# tuples.py

def format_record(rec):
    if len(rec) != 3:
        raise ValueError("Должно быть 3 элемента")
    
    fio, group, gpa = rec
    
    # Убираем лишние пробелы
    fio_clean = ' '.join(fio.split()).strip()
    group_clean = group.strip()
    
    if fio_clean == "":
        raise ValueError("ФИО не может быть пустым")
    
    # Разбиваем ФИО на части
    parts = fio_clean.split()
    
    # Формируем результат
    result = parts[0]  # Фамилия
    
    # Добавляем инициалы
    for i in range(1, len(parts)):
        if len(parts[i]) > 0:
            result += f" {parts[i][0].upper()}."
    
    # Форматируем GPA
    gpa_str = f"{gpa:.2f}"
    
    return f"{result}, гр. {group_clean}, GPA {gpa_str}"

# Проверка
if __name__ == "__main__":
    print("=== Проверка tuples.py ===")
    
    students = [
        ("Мустафаев Сухроб Мухаммадович ", "BIVT-25-4", 4.6),
        ("Рустамов Руслан ...", "BIVT-25-20", 5.0),
        (" Абдухакимов Шахзод Дийорович ", "ABB-01", 3.999),
    ]
    
    for student in students:
        formatted = format_record(student)
        print(f"{student} -> {formatted}")