import hashlib

'''
Регестрация и вход пользователя
'''


class DatabaseUser:
    dictionary_user = {}

    def add_user(self, nickname, password, age):
        self.dictionary_user[nickname] = password, age


class User:
    def __init__(self, nickname, password, password_confirm, age):
        if isinstance(nickname, str):
            self.nickname = nickname
        if len(password) >= 8:
            for symbol in password:
                if symbol.isalpha():
                    if symbol.isupper():
                        if password == password_confirm:
                            salt = b''
                            password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
                            self.password = password
                        break
        if age.isdigit() and int(age) > 0:
            self.age = age


database = DatabaseUser()
while True:
    choice = input("Выберите действие: \n1 - Вход\n2 - Регистрация\n3 - Выход\n")
    if choice.isdigit():
        choice = int(choice)
    else:
        continue
    if choice == 1:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        salt = b''
        password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        if login in database.dictionary_user:
            if password == database.dictionary_user[login][0]:
                print()
                print(f"Вход выполнен, {login}\n")
                break
            else:
                print("Неверный пароль.\n")
        else:
            print("Пользователь не найден.\n")
    elif choice == 2:

        user = User(input("Введите логин: "), input("Введите пароль: "), input("Введите проверку пароля: "),
                    input("age: "))
        try:
            if user.nickname not in database.dictionary_user:
                database.add_user(user.nickname, user.password, user.age)
                print(f"\nВход выполнен, {user.nickname}\n")
            else:
                print(f"Пользователь {user.nickname} уже существует")
        except:
            print("Вы ввели некоректные данные! Попробуйте снова.\n")

    elif choice == 3:
        exit()
