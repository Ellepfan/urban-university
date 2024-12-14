import sqlite3

def initiate_db():
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
    #                    (f"Product{i}", f"Описание{i}",
    #                     f"{i}00",))

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM Products").fetchall()
    # for info in products:
    #     print(f"Название: {info[1]} | Описание: {info[2]} | Цена: {info[3]}")
    connection.commit()
    connection.close()
    return products

def add_user(username, email, age):
    print(username, email, age)
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"{username}", f"{email}",
                    f"{age}", "1000"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()
    check_usnam = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_usnam.fetchone() is None:
        return True
    else:
        return False

    connection.commit()
    connection.close()

