# Цель:
# Написать программу на языке Python, используя Pycharm, для работы
# с неизменяемыми и изменяемыми объектами.
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'homework5.py'
# и напишите весь код в нём.
# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из
#   нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните,
#   почему нельзя изменить значения элементов кортежа.
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

immutable_var = "string", 1234, True, 3.2
print("immutable_var")
print(immutable_var)
print(type(immutable_var))
print(immutable_var*2)
# immutable_var[0] = 22 - кортеж неизменяемая коллекция, занимает меньше памяти чем списки которые можно изменять.
print()

print("mutable_list")
mutable_list = [2.3, False, 4321, "string"]
mutable_list[1] = True
mutable_list[-1] = "int"
print(mutable_list)
print(type(mutable_list))
print(mutable_list * 2)