# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.

from threading import Thread
from time import sleep
import random
from queue import Queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest: Guest | None = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        random_number = random.randint(3, 10)
        return sleep(random_number)


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tables

    def check_table(self):
        for table in self.tables:
            if table.guest == None:
                return table

    def check_table_guest(self):
        for table in self.tables:
            if table.guest != None:
                return table

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            if table := self.check_table():
                table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        try:
            while not self.queue.empty() or self.check_table_guest():
                for table in tables:
                    if self.check_table_guest() is  not None and not  self.check_table_guest().guest.is_alive():
                        print(f"{table.guest.name} за {table.number} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                    if not self.queue.empty() and self.check_table():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
        except:
            pass




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()
