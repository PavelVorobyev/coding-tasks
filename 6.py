# -*- coding: utf-8 -*-

# Текст задания в конце в виду его объема
# В задании не уточнено, какой объем входных данных предполагается. Поэтому скрипт тестировался
# примерно на 20млн записей.

from collections import Counter
import csv

USERS_FILE = 'users2.csv'

# Счетчик, в котором будет вестись количество вхождений доменов в файле
domain_counter = Counter()
users_list = list()

with open(USERS_FILE, 'rb') as uf:
    reader = csv.reader(uf, delimiter=',')
    next(reader)
    for email, user in reader:
        for z in range(5):
            _, domain = email.split('@')

            # Конструкция введена, чтобы не повторять код из блока try в блоке except
            for i in range(2):
                try:
                    users_list[domain_counter[domain]].append((email, user))
                except IndexError:
                    users_list.append(list())
                else:
                    break
            domain_counter.update([domain])


# Имеется csv-файл вида (данные не упорядочены):

# email,name
# test1@mail.ru,username1
# test2@gmail.com,username2
# test3@gmail.com,username3
# test4@rambler.ru,username4
# test5@ya.ru,username5
# ...
# testN@yahoo.com,usernameN
#
# Используя данные из csv-файла необходимо создать список, в котором будут
# содержаться группы кортежей вида (email, name) с условием, что в каждой
# группе почтовые домены не должны повторяться. Пример:
#
# [
#     [
#    	 ( ...@mail.ru, ... ),
#    	 ( ...@gmail.com, ... ),
#    	 ( ...@rambler.ru, ... ),
#    	 ( ...@ya.ru, ... ),
#    	 ( ...@..., ... ),
#    	 ( ...@yahoo.com, ... )
#     ],
#     [
#    	 ( ...@mail.ru, ... ),
#    	 ( ...@rambler.ru, ... ),
#    	 ( ...@ya.ru, ... ),
#    	 ( ...@..., ... )
#     ],
#     ...
#     [
#    	 ( ...@mail.ru, ... ),
#    	 ( ...@ya.ru, ... )
#     ]
# ]
#
# Решение должно быть оптимальным для использования больших объемов входных данных.
