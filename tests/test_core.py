from hypothesis import given
from hypothesis import strategies as st
from src.core import double_even_numbers

@given(st.lists(st.integers()))
def test_double_even_numbers_properties(nums):
    result = double_even_numbers(nums)
    
    # Свойство 1: Все элементы в результате должны быть четными
    assert all(x % 2 == 0 for x in result)
    
    # Свойство 2: Длина результата не может быть больше длины оригинала
    assert len(result) <= len(nums)
