def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    
    return (min(nums), max(nums))
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
def flatten(mat: list[list | tuple]) -> list:
    result = []
    
    for i, element in enumerate(mat):
        if not isinstance(element, (list, tuple)):
            raise TypeError(f"Элемент с индексом {i} не является списком или кортежем: {element}")
        
        result.extend(element)
    
    return result