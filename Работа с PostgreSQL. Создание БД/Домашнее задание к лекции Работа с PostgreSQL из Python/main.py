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
                name VARCHAR(35),
                last_name VARCHAR(35),
                email VARCHAR(255) UNIQUE
                );
        """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS telephone(
                id SERIAL PRIMARY KEY,
                contacts_id INTEGER,
                tel_number VARCHAR(12)
                );
    """)
    conn.commit()  # фиксируем в БД
    return '\n Создание структуры БД (Таблиц) создано.\n Приступайте к наполнению БД.'

class Client:
    def __init__(self, name, last_name, email, phone=None):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.client_info = self.name, self.last_name, self.email, self.phone

    def check_info(self):
        print(self.name, self.last_name, self.email, self.phone)

    def add_client(self, conn,):
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO contacts(name, last_name, email)
        VALUES (%s, %s, %s);
        """, (self.name, self.last_name, self.email))
        conn.commit()  # фиксируем в БД

        cur.execute("""
        SELECT id FROM contacts
        WHERE email = %s;
        """, (self.email,))
        client_id = cur.fetchone()
        if self.phone:
            cur.execute("""
                INSERT INTO telephone(contacts_id, tel_number)
                VALUES (%s, %s);
                """, (client_id, self.phone))
        conn.commit()  # фиксируем в БД

        return print(f'\nзапись "{" ".join(self.client_info)}" внесена в БД')



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
        print(f'\nВведите cr - чтобы создать структуру БД (таблицы) '
            f'\nвведите ad - чтобы добавить нового клиента '
            f'\nвведите adt - чтобы добавить телефон для существующего клиента '
            f'\nвведите a - чтобы изменить данные о клиенте '
            f'\nвведите a - удалить телефон для существующего клиента '  
            f'\nвведите a - удалить существующего клиента ' 
            f'\n* - завершить работу')
        letter = input('Введите название команды: ')
        if letter == 'cr':
            print(f'\nВнимание создание структуры БД приведет к уничтожению всех ранее введенных данных'
                f'\nвведите p - чтобы продолжить'
                f'\n* - вернуться в главное меню')
            answer = input('Введите название команды: ')
            if answer == 'p':
                create_db(conn)
            elif answer == '*':
                continue
        elif letter == 'ad':
            print('\nВнесите сведения о новом клиенте:')
            new_client = Client(input('Имя: '), input('Фамилия: '), input('email: '), input('Телефон: '))
            new_client.add_client(conn)
        elif letter == 'adt':
            print('\nВнесите сведения о клиенте и номер телефона:')
        #     list_doc()
        # elif letter == 'a':
        #     add_doc()
        elif letter == '*':
            sys.exit()

    conn.close()
