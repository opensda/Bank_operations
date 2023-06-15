from pathlib import Path

from utils import read_operations, get_pure_operations, get_lst_5_oper_srtd, get_hidden_data,\
    print_lst_5_opn

DATA_FOLDER = Path("C:/Users/Петр Иванов/PycharmProjects/pythonProject4/src")
FILE_TO_OPEN = DATA_FOLDER / "operations.json"


if __name__ == '__main__':
    operations = read_operations(FILE_TO_OPEN)
    pure_operations = get_pure_operations(operations)
    oper_srtd_by_date = get_lst_5_oper_srtd(pure_operations)
    hidden_data_operations = get_hidden_data(oper_srtd_by_date)
    print_lst_5_opn(hidden_data_operations)
