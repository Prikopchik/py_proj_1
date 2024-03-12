from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_get_invalid_index():
    assert arrs.get([1, 2, 3], 10, "test") == "test"

def test_slice_none_arguments():
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_slice_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]

def test_slice_negative_end():
    assert arrs.my_slice([1, 2, 3, 4], end = -1) == [1, 2, 3]

def test_my_slice_empty_list():
    result = arrs.my_slice([], 0, 1)
    assert result == []