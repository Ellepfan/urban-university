# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.


def is_prime(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        for i in range(2, result_func):
            if result_func % i == 0:
                print("Составное")
        else:
            print("Простое")
        return result_func

    return wrapper


@is_prime
def sum_three(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


result = sum_three(2, 3, 6)
print(result)
