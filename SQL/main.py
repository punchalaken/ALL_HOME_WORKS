import psycopg2

class ClientInf:
    def __init__(self, conn):
        self.conn = conn

    def create_db(self):
        with self.conn.cursor() as cur:
            cur.execute('''
                DROP TABLE phone_number;
                DROP TABLE client;
                ''')
            cur.execute('''
                    CREATE TABLE IF NOT EXISTS client(client_id SERIAL PRIMARY KEY,
                    name VARCHAR(30) NOT NULL,
                    surname VARCHAR(30) NOT NULL,
                    email VARCHAR(50) NOT NULL
                    );
                    ''')
            cur.execute('''
                    CREATE TABLE IF NOT EXISTS phone_number (
                    client_id INTEGER REFERENCES client(client_id),
                    phone_num VARCHAR(25),
                    CONSTRAINT check_phone_num CHECK (phone_num ~ '^(\\+?7|8)\\d{10}$')
                    );
                    ''')
            self.conn.commit()
        return print('Таблица успешно создана')

    def new_client(self, name, surname, email, phone_num=[]):
        with self.conn.cursor() as cur:
            cur.execute('''
                    INSERT INTO client(name, surname, email)
                    VALUES(%s, %s, %s)
                    RETURNING client_id;''', (name, surname, email))
            client_id = cur.fetchone()
            if phone_num==[]:
                cur.execute('''
                        INSERT INTO phone_number(client_id, phone_num)
                        VALUES(%s, NULL);
                        ''', (client_id,))
            elif len(phone_num) == 1:
                cur.execute('''
                        INSERT INTO phone_number(client_id, phone_num)
                        VALUES(%s, %s);
                        ''', (client_id, phone_num[0]))
            else:
                for num in phone_num:
                    cur.execute('''
                        INSERT INTO phone_number(client_id, phone_num)
                        VALUES(%s, %s);
                        ''', (client_id, num))
            self.conn.commit()

    def number_add(self, email, phone_num):
        with self.conn.cursor() as cur:
            cur.execute('''
                INSERT INTO phone_number(client_id, phone_num)
                VALUES((SELECT client_id FROM client WHERE email = %s), %s);
                ''', (email, phone_num))
            self.conn.commit()


    def client_update(self, client_id, name=None, surname=None, email=None, phone_num=None):
        with self.conn.cursor() as cur:
            if name is not None:
                cur.execute('''
                        UPDATE client
                        SET name = %s
                        WHERE client_id = %s;
                        ''', (name, client_id))
            if surname is not None:
                cur.execute('''
                        UPDATE client
                        SET surname = %s
                        WHERE client_id = %s;
                        ''', (surname, client_id))
            if email is not None:
                cur.execute('''
                        UPDATE client
                        SET email = %s
                        WHERE client_id = %s;
                        ''', (email, client_id))
            if phone_num is not None:
                cur.execute('''
                        UPDATE phone_number
                        SET phone_num = %s
                        WHERE client_id = %s;
                        ''', (phone_num, client_id))
            self.conn.commit()


    def del_phone(self, client_id):
        with self.conn.cursor() as cur:
            cur.execute('''
                    DELETE FROM phone_number
                    WHERE client_id = %s;
                    ''', (client_id,))

            self.conn.commit()
        return print('Вы отписались от рассылки, очень жаль =(')

    def del_client(self, client_id):
        with self.conn.cursor() as cur:
            cur.execute('''
                    DELETE FROM phone_number
                    WHERE client_id = %s;
                    ''', (client_id,))

            cur.execute('''
                    DELETE FROM client
                    WHERE client_id = %s;
                    ''', (client_id,))
            self.conn.commit()

        return print('Если мы снова понадобимся, мы будем ждать Вас!')

    def find_client(self, name=None, surname=None, email=None, phone_num=None):
        with self.conn.cursor() as cur:
            if name is not None:
                cur.execute('''
                        SELECT client_id
                        FROM client
                        WHERE name = %s;
                        ''', (name, ))
                return print(*cur.fetchone(), sep=', ')
            elif surname is not None:
                cur.execute('''
                        SELECT client_id
                        FROM client
                        WHERE surname = %s;
                        ''', (surname, ))
                return print(*cur.fetchone())
            elif email is not None:
                cur.execute('''
                        SELECT client_id
                        FROM client
                        WHERE email = %s;
                        ''', (email, ))
                return print(*cur.fetchone(), sep=', ')
            elif phone_num is not None:
                cur.execute('''
                        SELECT c.client_id
                        FROM client c
                        JOIN phone_number pn ON c.client_id = pn.client_id
                        WHERE phone_num = %s;
                        ''', (phone_num, ))
                return print(*cur.fetchone(), sep=', ')


conn = psycopg2.connect(database='clients', user='postgres', password='qQ02051971eE')
# Создаем класс CI
CI = ClientInf(conn)

# Создаем две таблицы, чтобы можно было записывать не один номер, а несколько.
# Используем тип связи - "Один ко многому"
CI.create_db()

# Добавляем несколько клиентов в наши таблицы.
CI.new_client('Семен', 'Клюев', 'penekkakti@gmail.com', ['+79111568371', '89111458371'])
CI.new_client('Артем', 'Кругляков', 'artem97@gmail.com', ['+79657909295'])
CI.new_client('Егор', 'Ожегов',  'egorkastar@gmail.com')

# Добавляем номер телефона по email. (Удаление происходит со тороны пользователя)
CI.number_add('penekkakti@gmail.com', '+79211293567')
CI.number_add('artem97@gmail.com', '+79211293567')

#Обновляем данные по id клиента.
CI.client_update(3, name='Евгений' ,phone_num='+79999999999')

# Удаляем телефон пользователя по его id.
CI.del_phone(3)

# Удаляем клиента по его id(удаление происходит сразу из двух таблиц).
CI.del_client(1)

# Находим клиента по заданным данным.
CI.find_client(name='Артем')
CI.find_client(surname='Кругляков')
CI.find_client(email='artem97@gmail.com')
CI.find_client(phone_num='+79657909295')

conn.close()
