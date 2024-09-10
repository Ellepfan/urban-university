import hashlib
import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    @staticmethod
    def password(password: str):
        salt = b''
        password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Конвертирование пароля в байты
            salt,
            100000
        )
        return password


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self) -> str:
        return f"{self.title}"


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None
        self.current_user_info = []

    def log_in(self, nickname, password):  # вход в пользователя
        for user in self.users:  # Проверка пароля пользователя
            if nickname == user:
                password_user = self.users[user][1]
                if password == password_user:
                    if user == nickname:
                        current_user_info = self.users[user]
                        self.current_user_info.clear()
                        self.current_user_info.extend([current_user_info])
                    self.current_user = nickname
                    print(f"Пользователь {self.current_user} выполнил вход")
                else:
                    print("Вы ввели не верный пароль")
                    continue

    def register(self, nickname, password, age):  # Регестрация пользователя
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return
        self.users[nickname] = nickname, password, age  # Добавление пользователя
        # в словарь список пользователей users = {}
        self.log_in(nickname, password)  # авто-логин зарегестрированного пользователя

    def log_out(self):  # выход  из пользователя
        if self.current_user != None:
            print(f"Вы вышли из пользователя {self.current_user}")
            self.current_user = None

    def add(self, *args: Video):
        for i in args:
            self.videos[i.title] = i.duration, i.time_now, i.adult_mode

    def get_videos(self, video_check: str):
        list_video = []
        for video in self.videos:
            video = str(video)
            if video_check.upper() in video.upper():
                list_video.append(video)
        if len(list_video) == 0:
            list_video.append("Совпадений не найдено")
        return list_video

    def watch_video(self, video):  # Воспроизведение видео для авторизованных пользователей
        # с фильтром по возрсту
        for name_video in self.videos.keys():
            if video == name_video:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                else:
                    for self.current_user in self.current_user_info:
                        for age_user in self.current_user_info:
                            if age_user[2] > 18:
                                print(f"Вы смотрите видео: {video}")
                                for i in range(1, self.videos[name_video][0] + 1):
                                    print(i, end=" ", sep=" ")
                                    time.sleep(1)

                                print()
                                print("Конец видео")
                            else:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")

                            self.current_user = age_user[0]


ur = UrTube()

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
ur.log_out()

# Проверка входа в другой аккаунт
ur.log_in('urban_pythonist', 'F8098FM8fjm9jmi')
print(ur.current_user)

ur.register('vasya_pupkin','F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.log_out()

ur.log_in('vasya_pupkin','')
print(ur.current_user)


ur.log_in('vasya_pupkin','lolkekcheburek')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
