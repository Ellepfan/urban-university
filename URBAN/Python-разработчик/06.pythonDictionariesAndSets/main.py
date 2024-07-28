# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему
#   из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите
#  значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.

my_dict = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
print(my_dict)

print(my_dict['apple'])

print(my_dict.get('chery', "такого ключа нет"))

my_dict ['grapefruit'] = 'fruit'
my_dict.update({'cherry ':'berry',
                'strawberry ':'berry'})

variable = my_dict.pop('apple')
print(variable)

print(my_dict)
print()

#
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных
#   с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.

my_set = {1,1,1,2,1,3,6,78,12,23,78}
print(my_set)

my_set.add(0)
my_set.add(100)
my_set.add(10)

my_set.discard(78)
my_set.remove(12)
my_set.pop()

print(sorted(my_set))