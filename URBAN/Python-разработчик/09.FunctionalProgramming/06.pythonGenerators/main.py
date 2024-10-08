# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.


def all_variants(text: str):
    for number in range(len(text)):
        for slice_number in range(len(text) - number):
            yield text[slice_number:slice_number + number + 1]


a = all_variants("abc")
for i in a:
    print(i)
