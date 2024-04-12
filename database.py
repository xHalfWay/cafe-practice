import sqlite3

conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

def authenticate_user(login, password):
    '''
    Функция `authenticate_user` выполняет аутентификацию пользователя в базе данных.
    Она получает логин и пароль, затем выполняет запрос к базе данных, чтобы найти пользователя с указанными учетными данными.
    :param login:
    :param password:
    :return:
    '''
    try:
        conn = sqlite3.connect('cafe.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
        user = cursor.fetchone()

        conn.close()
        return user
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None

# пользователи
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
                )''')

# заказы
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                table_number INTEGER NOT NULL,
                customer_count INTEGER NOT NULL,
                status TEXT NOT NULL
                )''')

# смены
cursor.execute('''CREATE TABLE IF NOT EXISTS shifts (
                id INTEGER PRIMARY KEY,
                shift_date DATE NOT NULL,
                shift_type TEXT NOT NULL
                )''')

conn.commit()
conn.close()
