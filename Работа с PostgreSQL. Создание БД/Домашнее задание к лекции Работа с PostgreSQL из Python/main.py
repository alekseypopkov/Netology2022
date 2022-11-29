import psycopg2
import sys

def create_db(conn):
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE telephone;
    DROP TABLE contacts;
    """)

    cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
                id SERIAL PRIMARY KEY,
                name VARCHAR(35) UNIQUE,
                last_name VARCHAR(35) UNIQUE,
                email VARCHAR(255) UNIQUE
                );
        """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS telephone(
                id SERIAL PRIMARY KEY,
                contactc_id INTEGER,
                tel_number INTEGER
                );
    """)
    conn.commit()  # фиксируем в БД
    return print('\n Создание структуры БД (Таблиц) создано.\n Приступайте к наполнению БД.')

def add_client(conn, first_name, last_name, email, phones=None):
    pass

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="clients_db", user="postgres", password="Alex1869") as conn:
    while True:
        print(f'\nВведите c - чтобы создать структуру БД (таблицы) '
            f'\nвведите s - чтобы узнать номер полки документа '
            f'\nвведите l - чтобы вывести список всех документов '
            f'\nвведите a - чтобы добавить новый документ '
            f'\n* - завершить работу')
        letter = input('Введите название команды: ')
        if letter == 'c':
            print(f'\nВнимание создание структуры БД приведет к уничтожению всех ранее введенных данных'
                f'\nвведите p - чтобы продолжить'
                f'\n* - вернуться в главное меню')
            answer = input('Введите название команды: ')
            if answer == 'p':
                create_db(conn)
            elif answer == '*':
                main()

        #     name_people()
        # elif letter == 's':
        #     search_shelf()
        # elif letter == 'l':
        #     list_doc()
        # elif letter == 'a':
        #     add_doc()
        elif letter == '*':
            sys.exit()

    conn.close()