import pytest
from model.calculator_model import add_list

def test_add_list_empty():
    assert add_list([]) == 0

def test_add_list_single_element():
    assert add_list([5]) == 5

def test_add_list_multiple_elements():
    assert add_list([1, 2, 3]) == 6

def test_add_list_negative_numbers():
    assert add_list([-1, -2, -3]) == -6

def test_add_list_mixed_positive_negative():
    assert add_list([-1, 2, -3, 4]) == 2

def test_add_list_large_numbers():
    assert add_list([10**6, 10**6]) == 2 * 10**6

def test_add_list_zero():
    assert add_list([0, 0, 0, 0]) == 0

def test_add_list_floats():
    assert add_list([1.5, 2.5, 3.5]) == 7.5

def test_add_list_mixed_types():
    with pytest.raises(TypeError):
        add_list([1, 'a', 3])

def test_add_list_nested_lists():
    with pytest.raises(TypeError):
        add_list([[1, 2], [3, 4]])

def test_add_list_invalid_input():
    with pytest.raises(TypeError):
        add_list(123)

def test_add_list_invalid_input_type():
    with pytest.raises(TypeError):
        add_list(None)
