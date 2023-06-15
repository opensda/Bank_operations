import pytest

from src.utils import read_operations, get_pure_operations, get_lst_5_oper_srtd, get_hidden_data
from pathlib import Path
from tests.data.data import tested_operation, operations_zero, tested_result, tested_operation_2, \
    tested_result_2, tested_operation_3, tested_result_3, pure_operations_ts, pure_operations_ts_rst, \
    hidden_test_data_1, hidden_test_result_1, hidden_test_data_2, hidden_test_result_2


def test_read_operations():
    test_value = 12
    data_folder = Path("C:/Users/Петр Иванов/PycharmProjects/pythonProject4/tests")
    file_to_open = data_folder / "yeti.json"
    assert read_operations(file_to_open) == test_value


def test_get_pure_operation():
    assert get_pure_operations(operations_zero) == []
    assert get_pure_operations(tested_operation) == tested_result
    assert get_pure_operations(tested_operation_2) == tested_result_2
    assert get_pure_operations(tested_operation_3) == tested_result_3


def test_get_lst_5_oper_srtd():
    pure_operations = pure_operations_ts
    assert get_lst_5_oper_srtd(pure_operations) == pure_operations_ts_rst


def test_get_hidden_data():
    assert get_hidden_data(hidden_test_data_1) == hidden_test_result_1
    assert get_hidden_data(hidden_test_data_2) == hidden_test_result_2



