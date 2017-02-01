# -*- coding: utf-8 -*-


# Имеются 2 таблицы — users и messages:
#
# users [ uid, name ]
# messages [ uid, msg ]
#
# Используя sqlite3 создайте базу данных и соответствующие таблицы (напишите SQL для создания
# таблиц). Напиши SQL-запрос, результатом которого будет выборка из двух полей:
# «Имя пользователя» и «Общее количество сообщений».


import sqlite3

DATABASE = 'consolo.db'
CREATE_QUERY = """
                CREATE TABLE users (
                    uid integer primary key unique,
                    name text
                );
                CREATE TABLE messages (
                    uid integer references users(uid),
                    msg text
                );
                """
SELECT_QUERY = """
                SELECT name
                     , IFNULL(q.msg_cnt, 0)
                FROM users
                LEFT JOIN
                    (SELECT uid
                          , COUNT(msg) as msg_cnt
                     FROM messages
                     GROUP BY 1) q
                    ON users.uid=q.uid
                """


def fill_db(cur):
    cur.execute('INSERT INTO users VALUES(1,"Anne");')
    cur.execute('INSERT INTO users VALUES(2,"Bet");')
    cur.execute('INSERT INTO users VALUES(3,"Carl");')
    cur.execute('INSERT INTO messages VALUES(1,"Hello");')
    cur.execute('INSERT INTO messages VALUES(1,"world");')
    cur.execute('INSERT INTO messages VALUES(1,"!");')
    cur.execute('INSERT INTO messages VALUES(3,"test");')


conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Условие, необходимое для рабоыт FOREIGN KEY
cursor.execute("PRAGMA foreign_keys = ON;")

# Создание схемы
cursor.executescript(CREATE_QUERY)

# Наполнение БД
fill_db(cursor)

# Получаем список пользователей и количество их сообщений
a = cursor.execute(SELECT_QUERY)
print(a.fetchall())
