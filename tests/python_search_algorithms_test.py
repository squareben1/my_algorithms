import pytest
from python_examples import PySearchAlgorithms

my_list = [1, 3, 5, 7, 9]

subject = PySearchAlgorithms()

class TestPySearchAlgorithms:
    def test_binary_search_3(self):
        assert subject.binary_search(my_list, 3) == 1
    def test_binary_search_9(self):
        assert subject.binary_search(my_list, 9) == 4