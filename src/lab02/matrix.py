# matrix.py

def transpose(mat):
    if len(mat) == 0:
        return []
    
    # Проверяем что все строки одинаковые
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Строки разной длины")
    
    # Создаем новую матрицу
    new_mat = []
    
    # Для каждого столбца
    for j in range(len(mat[0])):
        new_row = []
        # Для каждой строки
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        new_mat.append(new_row)
    
    return new_mat

def row_sums(mat):
    if len(mat) == 0:
        return []
    
    # Проверяем прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Строки разной длины")
    
    sums = []
    for row in mat:
        total = 0
        for num in row:
            total += num
        sums.append(float(total))
    
    return sums

def col_sums(mat):
    if len(mat) == 0:
        return []
    
    # Проверяем прямоугольность
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Строки разной длины")
    
    # Создаем список для сумм
    sums = [0] * len(mat[0])
    
    for row in mat:
        for j in range(len(row)):
            sums[j] += row[j]
    
    # Преобразуем в float
    return [float(x) for x in sums]

# Проверка
if __name__ == "__main__":
    print("=== Проверка matrix.py ===")
    
    test_matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"Матрица: {test_matrix}")
    print(f"Транспонированная: {transpose(test_matrix)}")
    print(f"Суммы строк: {row_sums(test_matrix)}")
    print(f"Суммы столбцов: {col_sums(test_matrix)}")