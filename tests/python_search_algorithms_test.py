import pytest
from python_examples import *

my_list = [1, 3, 5, 7, 9]
unordered_list = [3, 4, 2, 1, 4, 7]


def test_binary_search_3():
    assert binary_search(my_list, 3) == 1


def test_binary_search_9():
    assert binary_search(my_list, 9) == 4


def test_find_smallest():
    assert find_smallest(unordered_list) == 3  # returns smallest index


def test_selection_sort_ascending():
    assert selection_sort(unordered_list) == [1, 2, 3, 4, 4, 7]


# ----- Recursive Sum -----

def test_recursive_sum_return_zero():
    assert recursive_sum([]) == 0


def test_recursive_sum_return_one_len():
    assert recursive_sum([7]) == 7


def test_recursive_sum_return_two_len():
    assert recursive_sum([2, 4]) == 6


def test_recursive_sum_return_three_len():
    assert recursive_sum([2, 4, 6]) == 12

# --- Write a recursive function to count the number of items in a list ---


def test_recursive_list_count_1():
    assert recursive_count([]) == 0


def test_recursive_list_count_2():
    assert recursive_count([1, 2]) == 2

# --- Find the maximum number in a list ---


def test_recursive_max_num_1():
    assert recursive_max_num([1]) == 1


def test_recursive_max_num_2():
    assert recursive_max_num([1, 2]) == 2

def test_recursive_max_num_3():
    assert recursive_max_num([1, 2, 3]) == 3
