def min_max(nums):
    if len(nums) == 0:
        raise ValueError("Список пустой")
    
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
            
    return (min_num, max_num)

def unique_sorted(nums):
    if len(nums) == 0:
        raise ValueError("Список пустой")
    
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    
    unique_list.sort()
    return unique_list


def flatten(mat):
    result = []
    
    for element in mat:
        if not isinstance(element, [list, tuple]):
            raise TypeError("Нужен список или кортеж")
        
        for item in element:
            result.append(item)
              
    return result

# Проверка работы
if __name__ == "__main__":
    print("=== Проверка arrays.py ===")
    
    # Тестируем min_max
    test1 = [3, -1, 5, 5, 0]
    print(f"min_max({test1}) = {min_max(test1)}")
    
    # Тестируем unique_sorted
    test2 = [3, 1, 2, 1, 3]
    print(f"unique_sorted({test2}) = {unique_sorted(test2)}")
    
    # Тестируем flatten
    test3 = [[1, 2], [3, 4]]
    print(f"flatten({test3}) = {flatten(test3)}")