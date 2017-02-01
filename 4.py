# -*- coding: utf-8 -*-


# Имеется лог веб-сервера, где каждая строка соответствует одному обращению клиента к веб-серверу. Формат лога:
#
# ...
# 127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /index.php HTTP/1.0" 200 2326
# ...
#
# Найти пять IP-адресов, от которых было больше всего запросов.


from re import search
from collections import Counter

LOG_FILE = "access.log.1"
# regexp, найденный в одной из книг рецептов
IP_PATTERN = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# Счетчик
counter = Counter()

with open(LOG_FILE) as log:
    for line in log:
        s = search(IP_PATTERN, line)
        counter.update([s.group(0)])

# Топ-5 ip адресов по вхождению
top5 = counter.most_common(5)
print(top5)
