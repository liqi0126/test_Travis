# -*- coding: utf-8 -*-
import re
import datetime

ID_weight_table = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
ID_check_table = {
    0: '1',
    1: '0',
    2: 'X',
    3: '9',
    4: '8',
    5: '7',
    6: '6',
    7: '5',
    8: '4',
    9: '3',
    10: '2'
}


def register_params_check(content):
    if type(content) is not dict:
        return 'username', False

    # username
    username = content.get('username', None)

    if type(username) is not str:
        return 'username', False

    if len(username) < 6 or len(username) > 10:
        return 'username', False

    # password
    password = content.get('password', None)

    if type(password) is not str:
        return 'password', False

    if len(password) < 6 or len(password) > 18:
        return 'password', False

    if not re.search(r'[0-9]+', password):
        return 'password', False

    if not re.search(r'[a-z]+', password):
        return 'password', False

    if not re.search(r'[A-Z]+', password):
        return 'password', False

    if re.search(r'[^a-zA-Z0-9]+', password):
        return 'password', False

    # nickname
    nickname = content.get('nickname', None)

    if type(nickname) is not str:
        return 'nickname', False

    if len(nickname) < 2 or len(nickname) > 8:
        return 'nickname', False

    # document_number
    document_number = content.get('document_number', None)

    if type(document_number) is not str:
        return 'document_number', False

    if len(document_number) != 18:
        return 'document_number', False

    address_code = document_number[:6]

    if re.search(r'[^0-9]+', address_code):
        return 'document_number', False

    birthday_code = document_number[6:14]

    if re.search(r'[^0-9]+', birthday_code):
        return 'document_number', False

    year = int(birthday_code[:4])
    month = int(birthday_code[4:6])
    day = int(birthday_code[6:8])
    try:
        datetime.datetime(year=year, month=month, day=day)
    except:
        return 'document_number', False

    if month == 2 and day == 29:
        after18time = datetime.datetime(year=year + 18, month=3, day=1)
    else:
        after18time = datetime.datetime(year=year + 18, month=month, day=day)
    now = datetime.datetime.now()

    if now < after18time:
        return 'document_number', False

    order_code = document_number[14:17]

    if re.search(r'[^0-9]+', order_code):
        return 'document_number', False

    check_code = document_number[17]
    sum = 0
    for code_id, code in enumerate(document_number[:-1]):
        sum += int(code) * ID_weight_table[code_id]
    if check_code != ID_check_table[sum % 11]:
        return 'document_number', False

    # mobile
    mobile = content.get('mobile', None)

    if type(mobile) is not int:
        return 'mobile', False

    if len(str(mobile)) != 11:
        return 'mobile', False

    # email

    email = content.get('email', None)

    if type(email) is not str:
        return 'email', False

    email = email.split('@')

    if len(email) != 2:
        return 'email', False

    if len(email[0]) <= 0 or len(email[0]) > 63:
        return 'email', False

    if re.search(r'[^a-zA-Z0-9]+', email[0]):
        return 'email', False

    hosts = email[1]

    if '.' not in hosts:
        return 'email', False

    if len(hosts) <= 0 or len(hosts) > 63:
        return 'email', False

    hosts = hosts.split('.')

    for host_idx, host in enumerate(hosts):
        if len(host) <= 0:
            return 'email', False

        if host[0] == '-':
            return 'email', False

        if host[-1] == '-':
            return 'email', False

        if re.search(r'[^a-zA-Z0-9\-]+', host):
            return 'email', False

        if host_idx == len(hosts) - 1:
            if not re.search(r'[^0-9]+', host):
                return 'email', False

    return "ok", True
