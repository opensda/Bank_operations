import pytest
from src.utils import read_operations

s = 12
def test_read_operations():
    path = 'yeti.json'
    assert read_operations(path) == s

