# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа)
# в качестве аргумента и проводит интроспекцию этого объекта,
# чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python
# для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте,
# включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
from pprint import pprint
import inspect


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


def introspection_info(obj):
    my_list = []
    my_list.append('Имя: '+ str(obj.__name__))
    my_list.append('тип: ' + str(type(obj)))
    my_list.append('атрибуты: ' + str(dir(obj)))
    my_list.append('методы: ' + str(inspect.getmembers(obj, inspect.isfunction)))
    my_list.append('Модуль, к которому объект принадлежит: ' + str(inspect.getmodule(obj)))
    my_list.append('Полная спецификация: '+ str(inspect.getfullargspec(obj)))
    my_list.append('Это функция?: ' + str(inspect.isfunction(obj)))
    return my_list


number_info = introspection_info(House)
pprint(number_info)
