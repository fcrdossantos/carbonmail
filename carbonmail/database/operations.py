import sqlite3


def create(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print("Ops... Deu um erro criando a tabela:", e)


def insert(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as e:
        print("Ops... Deu um erro inserindo dados:", e)


def delete(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as e:
        print("Ops... Deu um erro deletando dados:", e)


def select(connection, sql):
    result = None
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print("Ops... Deu um erro exibindo dados:", e)
    finally:
        return result
