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

# initiate_db()