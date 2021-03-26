import sqlite3
import sys, os
from carbonmail.utils import root_folder


def get_db_file():
    db_folder = os.path.join(root_folder(), "database")

    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    return os.path.join(db_folder, "contacts.db")


def connect():
    connection = None
    try:
        connection = sqlite3.connect(get_db_file())
        connection.execute("PRAGMA foreign_keys = 1")
    except sqlite3.Error as e:
        print("Ops... Deu um erro iniciando a connection:", e)

    return connection


def close_connection(connection):
    if connection:
        connection.close()
