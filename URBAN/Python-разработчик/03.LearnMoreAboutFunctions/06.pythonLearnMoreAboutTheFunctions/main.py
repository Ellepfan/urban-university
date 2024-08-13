# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные,
# что иногда по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы
# (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта
# суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре
# (списку, словарю и т.д.) по-разному.
#
# Ученику пришлось каждый раз использовать индексацию и обращение по
# ключам - универсального решения для таких структур он не нашёл.
#
# Помогите сокурснику осуществить его задумку.
#
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99


summa = 0


def chek_int(value):
    if not isinstance(value, int):
        for i in value:
            calculate_structure_sum(i)


def calculate_structure_sum(*values):
    global summa
    for value in values:
        if isinstance(value, int):
            summa = summa + value
            return summa

        elif isinstance(value, str):
            summa = summa + len(value)
            return summa

        elif isinstance(value, dict):
            pairs = list(value.items())
            chek_int(pairs)

        elif isinstance(value, tuple):
            if not isinstance(value, int):
                for i in value:
                    calculate_structure_sum(i)

        elif isinstance(value, list):
            chek_int(value)

        elif isinstance(value, set):
            chek_int(value)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
