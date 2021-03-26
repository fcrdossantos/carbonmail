import sqlite3
import sys, os


def get_db_file():
    try:
        sFile = os.path.abspath(sys.modules["__main__"].__file__)
    except:
        sFile = sys.executable
    return os.path.join(os.path.dirname(sFile), os.pardir, "contacts.db")


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


def create_table(connection, sql_create_table):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except sqlite3.Error as e:
        print("Ops... Deu um erro criando a tabela:", e)


def insert(connection, sql_insert_contact):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_contact)
        connection.commit()
    except sqlite3.Error as e:
        print("Ops... Deu um erro inserindo dados:", e)


def search(connection, sql_list_contacts):
    result = None
    try:
        cursor = connection.cursor()
        cursor.execute(sql_list_contacts)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print("Ops... Deu um erro exibindo dados:", e)
    finally:
        return result


def initialize():
    # Iniciando a Conexão
    connection = connect()

    sql_create_table_lists = """ CREATE TABLE IF NOT EXISTS list (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text NOT NULL
                            ); """

    # Criando a tabela
    sql_create_table_contact = """ CREATE TABLE IF NOT EXISTS contact (
                            id integer PRIMARY KEY AUTOINCREMENT,
                            name text NOT NULL,
                            email text NOT NULL,
                            list_id integer NOT NULL,
                            FOREIGN KEY(list_id) REFERENCES list(id)
                        ); """

    create_table(connection, sql_create_table_lists)
    create_table(connection, sql_create_table_contact)

    sql_insert_list_jpfp = "INSERT INTO list (name) VALUES ('Alunos Jornada')"
    sql_insert_list_alunos = "INSERT INTO list (name) VALUES ('Alunos Curso')"
    sql_insert_list_adm = "INSERT INTO list (name) VALUES ('Administradores')"

    insert(connection, sql_insert_list_jpfp)
    insert(connection, sql_insert_list_alunos)
    insert(connection, sql_insert_list_adm)

    # Inserindo alunos
    sql_insert_contact_felipe = "INSERT INTO contact (name, email, list_id) VALUES ('Felipe1','fcrdossantos@gmail.com.br', 1)"
    sql_insert_contact_felipe2 = "INSERT INTO contact (name, email, list_id) VALUES ('Felipe2','fcrdossantos@gmail.com.br', 2)"
    sql_insert_contact_felipe3 = "INSERT INTO contact (name, email, list_id) VALUES ('Felipe3','fcrdossantos@gmail.com.br', 3)"

    insert(connection, sql_insert_contact_felipe)
    insert(connection, sql_insert_contact_felipe2)
    insert(connection, sql_insert_contact_felipe3)

    # Buscando alunos
    sql_show_lists = "SELECT * FROM list"

    lists = search(connection, sql_show_lists)
    print(lists)

    sql_show_contacts = "SELECT contact.name, contact.email, list.name from contact, list where contact.list_id = list.id;"

    #

    contacts = search(connection, sql_show_contacts)

    # Fechando a Conexão
    close_connection(connection)

    # Mostrando os alunos
    for contact in contacts:
        print(
            f"O contato {contact[0]} tem o e-mail {contact[1]} e está na lista {contact[2]}"
        )
