import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    # Словарь: список пользователей
    users = {}
    # Словарь: список загруженных видео
    videos = {}
    # текущий пользователь - только имя
    current_user = None
    # список: полная информация текущего пользователя
    current_user_info = []

    def log_in(self, password, age=None):  # вход в пользователя
        for user in UrTube.users:  # Проверка пароля пользователя
            if self == user:
                if age == None:
                    salt = b''
                    password = hashlib.pbkdf2_hmac(
                            'sha256',
                        password.encode('utf-8'),  # Конвертирование пароля в байты
                        salt,
                            100000
                    )
                password_user = UrTube.users[user][1]
                if password == password_user:
                    if user == self:
                        current_user_info = UrTube.users[user]
                        UrTube.current_user_info.clear()
                        UrTube.current_user_info.extend([current_user_info])
                    UrTube.current_user = self
                    print(f"Пользователь {UrTube.current_user} выполнил вход")
                else:
                    print("Вы ввели не верный пароль")
                    continue


    def register(self, password, age):  # Регестрация пользователя
        if self in UrTube.users:
            print(f"Пользователь {self} уже существует")
            return
        else:  # хэширование пароля
            salt = b''
            password = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),  # Конвертирование пароля в байты
                salt,
                100000
            )
        UrTube.users[self] = self, password, age  # Добавление пользователя
        # в словарь список пользователей users = {}
        UrTube.log_in(self, password, age)  # авто-логин зарегестрированного пользователя

    @classmethod
    def log_out(cls, classmethod):  # выход  из пользователя
        if classmethod != None:
            print(f"Вы вышли из пользователя {classmethod}")
            UrTube.current_user = None

    @classmethod
    def add(cls, *video):  # Добавление видео в словарь загруженных видео videos = {}
        for i in video:
            if i.title not in UrTube.videos:
                UrTube.videos[i.title] = i.duration, i.time_now, i.adult_mode

    def get_videos(self):  # поиск видео по имени в словаре загруженных видео videos = {}
        list_video = []
        for video in UrTube.videos:
            video = str(video)
            if self.upper() in video.upper():
                list_video.append(video)
        if len(list_video) == 0:
            list_video.append("Совпадений не найдено")
        return list_video

    def watch_video(self):  # Воспроизведение видео для авторизованных пользователей
        # с фильтром по возрсту
        for name_video in UrTube.videos.keys():
            if self == name_video:
                if UrTube.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                else:
                    for UrTube.current_user in UrTube.current_user_info:
                        for age_user in UrTube.current_user_info:
                            if age_user[2] > 18:
                                print(f"Вы смотрите видео: {self}")
                                for i in range(1, UrTube.videos[name_video][0] + 1):
                                    print(i, end=" ", sep=" ")
                                    time.sleep(1)

                                print()
                                print("Конец видео")
                            else:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")

                            UrTube.current_user = age_user[0]


ur = UrTube

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)
#
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('коШ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out(UrTube.current_user)

# Проверка входа в другой аккаунт
ur.log_in('urban_pythonist', 'F8098FM8fjm9jmi')
print(ur.current_user)

ur.register('vasya_pupkin','F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.log_out(UrTube.current_user)

ur.log_in('vasya_pupkin','')
print(ur.current_user)


ur.log_in('vasya_pupkin','lolkekcheburek')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')