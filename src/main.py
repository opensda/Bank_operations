from pathlib import Path

from utils import read_operations, get_pure_operations, get_lst_5_oper_srtd, get_hidden_data,\
    print_lst_5_opn

PATH = "operations.json"


if __name__ == '__main__':
    """
    Программа выводит 5 последних успешных банковских операций клиента
    """

    # Считываем операции с файла данными

    operations = read_operations(PATH)

    # Оставляем, только те операции, в которых есть все необходимые данные:
    # id транзакции, статус перевода, сумма операции и валюта, описание типа перевода,
    # откуда (если имеется!) и куда был осуществлен перевод

    pure_operations = get_pure_operations(operations)

    # Получаем 5 последних успешных операций, отсортированных по дате

    oper_srtd_by_date = get_lst_5_oper_srtd(pure_operations)

    # Производим маскировку номеров счетов и карт

    hidden_data_operations = get_hidden_data(oper_srtd_by_date)

    # Выводим 5 последних успешных операций

    print_lst_5_opn(hidden_data_operations)
