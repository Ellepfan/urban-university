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


class Figure:
    sides_count = 0
    sides_value = 1

    def __init__(self, color: list, sides):
        self.list_sides = []
        if len(sides) == self.sides_count:
            for s in sides:
                self.list_sides.append(s)
        else:
            for i in range(1, self.sides_count + 1):
                self.list_sides.append(self.sides_value)
        sides = self.list_sides
        self.__sides = sides
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = None
        self.filled = bool

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(color):
        check_color = True
        for i in color:
            if isinstance(i, int) and 0 <= i <= 255:
                continue
            else:
                check_color = False
                break
        return check_color

    def set_color(self, r: int, g: int, b: int):
        list_color = [r, g, b]
        if self.__is_valid_color(list_color):
            self.__color = r, g, b
            return self.__color

    def __is_valid_sides(self, args):
        check_sides = False
        if len(args) == len(self.__sides):
            for i in args:
                if isinstance(i, int) and i > 0:
                    check_sides = True
        return check_sides

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.list_sides.clear()
            for s in new_sides:
                self.list_sides.append(s)
            self.__sides = self.list_sides
            return self.__sides

    def __len__(self):
        perimetr = 0
        for i in self.__sides:
            perimetr += i
        return perimetr


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, *sides):
        super().__init__(color, sides)
        for i in self.get_sides():
            self.__radius = i / (math.pi * 2)

    def get_square(self):
        square = 2 * math.pi * self.__radius
        return format(square, '.3')


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, *sides):
        super().__init__(color, sides)
        self.sides = self.get_sides()
        if self.get_sides()[0] + self.get_sides()[1] > self.get_sides()[2] and self.get_sides()[0] + self.get_sides()[
            2] > self.get_sides()[1] and self.get_sides()[1] + self.get_sides()[2] > self.get_sides()[0]:
            self.sides = sides
        else:
            self.list_sides.clear()
            for i in range(1, self.sides_count + 1):
                self.list_sides.append(self.sides_value)
        sides = self.list_sides
        self.__sides = sides

    def get_square(self):
        sum_sides = 0
        for i in self.get_sides():
            sum_sides += i
        p = 0.5 * sum_sides
        square = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return format(square, '.3')


#
#
class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:
            self.list_sides = []
            self.sides_value = sides
            if len(sides) == self.sides_count:
                for s in sides:
                    self.list_sides.append(s)
            else:
                for i in range(1, self.sides_count + 1):
                    self.list_sides.append(self.sides_value[0])
        self.__sides = self.list_sides

    def get_volume(self):
        volume_cube = self.__sides[0] ** 3
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

print()

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((32, 0, 12), 5, 6, 4)
circle2 = Circle((100, 100, 100), 10, 15, 6)
circle3 = Circle((200, 200, 100), 6)
triangle3 = Triangle((200, 200, 100), 10, 6)
cube4 = Cube((200, 200, 100), 9)
cube3 = Cube((200, 200, 100), 9, 12)
triangle2 = Triangle((0, 0, -1), 5)
cube2 = Cube((300, 0, 130), 2)
triangle4 = Triangle((0, 0, 2), 5, 43, 6)

print("Проверка на присвоение")
print(circle1.get_color())
print(triangle1.get_color())
print(triangle2.get_color())
print(cube1.get_color())
print(cube2.get_color())

print("Проверка на изменение цветов: ")
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
print(triangle1.get_color())
triangle1.set_color(255, -4, 255)
print(triangle1.get_color())
triangle1.set_color(255, 255, 255)
print(triangle1.get_color())

print("Проверка на изменение сторон: ")
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
cube2.set_sides(5, 3, 12, 4, 5, 3, 4, 5, 6, 7, 8, 12)
print(cube2.get_sides())
cube3.set_sides(5, 3, 12)
print(cube3.get_sides())
print()
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
circle2.set_sides(15, 22)  # Изменится
print(circle2.get_sides())
print()
triangle1.set_sides(2, 3, 4)
print(triangle1.get_sides())
triangle2.set_sides(10, 10, 12)
print(triangle2.get_sides())
triangle2.set_sides(1, 143, 2, 23)
print(triangle3.get_sides())

print("Проверка периметра, это и есть длина: ")
print("circle")
print(len(circle1))
print(len(circle2))
print("triangle")
print(len(triangle1))
print(len(triangle2))
print("cube")
print(len(cube1))
print(len(cube2))
print(len(cube3))

print("Проверка объёма (куба): ")
print(cube1.get_volume())
print(cube2.get_volume())
print(cube3.get_volume())
print(cube4.get_volume())

print("Площадь круга")
print(circle1.get_square())
print(circle2.get_square())
print(circle3.get_square())

print("Площадь треугольника")
print(triangle1.get_square())
print(triangle2.get_square())
print(triangle3.get_square())
print(triangle4.get_square())
