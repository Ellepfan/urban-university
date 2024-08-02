# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа
# из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True
# перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes
# и not_primes в зависимости от значения переменной is_prime после проверки
# (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
min_divisor = 2
max_divisor = 10

for is_prime in numbers:
    if is_prime != 1:
        for i in range(min_divisor, max_divisor + 1):
            if i != is_prime and i != max_divisor:
                if is_prime % i == 0:
                    flag = True
                    if flag == True:
                        not_primes.append(is_prime)
                        break
                    primes.append(is_prime)
            else:
                primes.append(is_prime)
                break

print("primes: ", primes)
print("not_primes: ", not_primes)


