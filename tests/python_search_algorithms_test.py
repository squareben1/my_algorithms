import pytest
from python_examples import PySearchAlgorithms

my_list = [1, 3, 5, 7, 9]
unordered_list = [3, 4, 2, 1, 4, 7]

subject = PySearchAlgorithms()

class TestPySearchAlgorithms:
    def test_binary_search_3(self):
        assert subject.binary_search(my_list, 3) == 1
    def test_binary_search_9(self):
        assert subject.binary_search(my_list, 9) == 4
    def test_find_smallest(self):
        assert subject.find_smallest(unordered_list) == 3
    def test_selection_sort_ascending(self):
        assert subject.selection_sort(unordered_list) == [1, 2, 3, 4, 4, 7]
    