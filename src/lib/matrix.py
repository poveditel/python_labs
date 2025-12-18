def min_max(matrix):
    if not matrix:
        return "ValueError"
    return (min(matrix), max(matrix))


def unique_sorted(matrix):
    if not matrix:
        return "ValueError"
    return sorted(list(set(matrix)))


def flatten(matrix):
    new_list = []
    for i in matrix:
        if type(i) is not list:
            if isinstance(i, tuple):
                new_list += list(i)
            else:
                return "ValueError"
        else:
            new_list += i
    return new_list


def check(matrix):
    if not matrix:
        return True
    k = len(matrix[0])
    for i in matrix:
        if len(i) != k:
            return False
    return True


def transpose(matrix: list[list[float | int]]) -> list[list]:
    if not check(matrix):
        return "ValueError"
    if not matrix:
        return []
    new_list = []
    new_list = [[] for i in range(len(matrix[0]))]
    for i in matrix:
        n = 0
        for j in i:
            new_list[n].append(j)
            n += 1
    return new_list


def row_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix):
        return "ValueError"
    if not matrix:
        return "ValueError"
    new_list = []
    for i in matrix:
        new_list.append(sum(i))
    return new_list


def col_sums(matrix: list[list[float | int]]) -> list[float]:
    if not check(matrix):
        return "ValueError"
    if not matrix:
        return "ValueError"
    return row_sums(transpose(matrix))
