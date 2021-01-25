"""
Тесты
"""
import sorting
import pytest

def test_bubble_smoke():
    test_list = [3, -1, 4, 5, -22, 8, 9, 6, 7]
    result = sorting.bubble_sort(test_list)
    test_list.sort()
    assert result == test_list


def test_bubble_empty():
    test_list = []
    result = sorting.bubble_sort(test_list)
    assert result == []


def test_bubble_negative():
    test_list = []
    result = sorting.bubble_sort(test_list)
    assert result == []


def test_bubble_not_integer():
    test_list = [3, -1, 4, 5, '-2', 8, 9, 6, 7]
    with pytest.raises(RuntimeError):
        sorting.bubble_sort(test_list)



