def double_even_numbers(numbers: list[int]) -> list[int]:
    """Возвращает список только четных чисел, умноженных на два."""
    return [num * 2 for num in numbers if num % 2 == 0]