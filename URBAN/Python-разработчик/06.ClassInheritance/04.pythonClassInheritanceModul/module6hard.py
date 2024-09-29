# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем,
# 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков
# программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты,
# но... Что лежит в основе удобного использования таких объектов?
# По названию задачи можно понять, что все геометрические фигуры обладают
# схожими свойствами, такими как: длины сторон, цвет и др.
#
# Давайте попробуем реализовать простейшие классы для некоторых таких
# фигур и при этом применить наследование (в будущем, изучая сторонние
# библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
import math
from typing import Tuple, Any


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides):
        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]
        if not isinstance(sides[0], int):
            for i in sides:
                sides = i
        if len(sides) != self.sides_count:
            self.__sides = []
        else:
            self.__sides = list(sides)
        self.filled = bool

    @staticmethod
    def isinstance_int(value):
        isinstance_int = False
        if isinstance(value, int):
            isinstance_int = True
        return isinstance_int

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        check_color = True
        for i in color:
            if self.isinstance_int(i) and 0 <= i <= 255:
                continue
            else:
                check_color = False
                break
        return check_color

    def set_color(self, r: int, g: int, b: int):
        list_color = [r, g, b]
        if self.__is_valid_color(list_color):
            self.__color = list_color
        return self.__color

    def __is_valid_sides(self, sides):
        check_sides = False
        if len(sides) == len(self.__sides):
            for i in sides:
                if self.isinstance_int(i) and i > 0:
                    check_sides = True
                else:
                    break
        return check_sides

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides) and self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i

        return perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, *sides):
        if len(sides) != 1:
            sides = 1
        else:
            for sides_int in sides:
                sides = sides_int
        super().__init__(color, sides)
        self.__radius = sides / (math.pi * 2)

    def get_square(self):
        square = math.pi * (self.__radius ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, *sides):
        super().__init__(color, sides)

    def get_square(self):
        sum_sides = 0
        for i in self.get_sides():
            sum_sides += i
        p = 0.5 * sum_sides
        square = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return square


#
#
class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        super().__init__(color, sides)
        if len(sides) != 1:
            self.sides = [1] * self.sides_count
        else:
            self.sides = list(sides) * self.sides_count

    def get_sides(self):
        return self.sides

    def get_volume(self):
        volume_cube = self.sides[0] ** 3
        return volume_cube


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
