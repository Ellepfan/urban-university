import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com",
                    f"{i}0", "1000"))
for j in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (f"{500}", f"User{j}"))
for k in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{k}",))

cursor.execute("DELETE FROM Users WHERE id = ?", (f"6"))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
# print(total_users)

cursor.execute("SELECT SUM (balance) FROM Users")
sum_balance = cursor.fetchone()[0]
# print(sum_balance)

print(sum_balance / total_users)

cursor.execute(f"SELECT username , email, age, balance FROM Users WHERE age !=?", (f"{60}",))
users = cursor.fetchall()

connection.commit()
connection.close()
