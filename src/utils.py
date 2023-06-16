import json
from datetime import datetime

def read_operations(path):
    """
    Читаем файл json
    :param file_to_open: имя файла (путь)
    :return: содержимое json-файла
    """
    with open(path, encoding='utf-8') as file:
        content = file.read()
        operations = json.loads(content)
        return operations

def get_pure_operations(operations):
    """
    Очищаем список словарей от мусора -
    удаляем пустые словари, неполноценные записи,
    оставляем только записи с ключами, согласно заданию
    :param operations: список со всеми операциями
    :return:  список операций с нужными ключами
    """
    pure_operations = []

    # Перебираем операции и пропускаем те,
    # у которых отсутствует заданный ключ

    for operation in operations:
        if operation.get('id') == None:
            continue
        elif operation.get('state') == None:
            continue
        elif operation.get('date') == None:
            continue
        elif operation.get('operationAmount') == None:
            continue
        elif operation.get('description') == None:
            continue
        elif operation.get('from') == None:
            continue
        elif operation.get('to') == None:
            continue
        pure_operations.append(operation)
    return pure_operations

def get_lst_5_oper_srtd(pure_operations):
    """
    Сортируем список и получаем 5 последниих
    операций со статусом 'EXECUTED'
    :param pure_operations: список операций
    :return: список 5 последних операций, отсортированных
    по дате (сверху самые последние операции)
    """
    just_date = []
    for operation in pure_operations:

        # Отбираем 5 последних дат, в которые успешно прошли операции: 'EXECUTED',
        # записываем их в список, и сортируем по убыванию

        if operation['state'] == 'EXECUTED':
            just_date.append(operation['date'])
    just_date.sort()
    just_date.reverse()
    lst_5_dates = just_date[:5]
    lst_5_operations = []

    # Записываем в список операции за 5 последних дат,
    # сортируем их по дате


    for operation in pure_operations:
        for date in lst_5_dates:
            if operation.get('date') == date:
                lst_5_operations.append(operation)

    oper_srtd_by_date = sorted(lst_5_operations, key=lambda d: d['date'])
    oper_srtd_by_date.reverse()

    return oper_srtd_by_date

def get_hidden_data(oper_srtd_by_date):
    """
    Маскируем конфиденциальные данные карт и счетов
    :param oper_srtd_by_date: список операций
    :return: список операций с замаскированными данными
    """
    for operation in oper_srtd_by_date:

        # Маскировка для счета отправителя

        if operation["from"].startswith('Счет'):
            bill = operation["from"]

            # Выделяем из строки номер счета

            bill_number = bill.split()[-1]

            # Маскируем номер счета (в формате **0000)
            # записываем его информацию о переводе по ключу

            private_bill_number = (len(bill_number[-6:-4]) * '*') + bill_number[-4:]
            private_bill = bill.split()[0] + " " + private_bill_number
            operation["from"] = private_bill

            # Маскировка для карты отправителя
        else:
            card = operation["from"]

            # Выделяем из строки номер карты

            card_number = card.split()[-1]

            # Маскируем номер карты (в формате  00** **** 0000)
            # записываем его информацию о переводе по ключу

            private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number), len(private_number) // 4
            private_sep_number = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
            private_card = card.split()[0] + " " + private_sep_number
            operation["from"] = private_card

        # Далее аналогичные операции по счетам и картам для получателя

        if operation["to"].startswith('Счет'):
            bill = operation["to"]
            bill_number = bill.split()[-1]
            private_bill_number = (len(bill_number[-6:-4]) * '*') + bill_number[-4:]
            private_bill = bill.split()[0] + " " + private_bill_number
            operation["to"] = private_bill

        else:
            card = operation["to"]
            card_number = card.split()[-1]
            private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number), len(private_number) // 4
            private_sep_number = " ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
            private_card = card.split()[0] + " " + private_sep_number
            operation["to"] = private_card
    hidden_data_operations = oper_srtd_by_date
    return hidden_data_operations

def print_lst_5_opn(hidden_data_operations):
    """
    Печатаем данные в формате, согласно заданию
    :param hidden_data_operations: список операций
    """
    for operation in hidden_data_operations:
        fine_date = datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')
        print (f'{fine_date:%d.%m.%Y} {operation["description"]}\n'
              f'{operation["from"]} --> {operation["to"]}\n'
              f'{operation["operationAmount"]["amount"]} '
              f'{operation["operationAmount"]["currency"]["name"]}\n'
              f'')