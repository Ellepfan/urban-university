# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной
# вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота
# (выход из ловушки) с двумя каменными вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом,
# а второе было всегда пустым.
#
# К вашему счастью рядом с менее успешными и уже неговорящими
# путешественниками находился папирус, где были написаны правила для решения этого
# "ребуса". (Как жаль, что они поняли это так поздно :( ).
# Во вторую вставку нужно было написать те пары чисел друг за другом,
# чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
# К сожалению, у вас не так много времени, чтобы подбирать пароль вручную,
# шипы сверху уже движутся на вас (обожаю клише), тем более числа в первой
# вставке будут попадаться случайно.
# Составьте алгоритм, используя циклы, чтобы в независимости от введённого
# числа n (от 3 до 20) программа выдавала нужный пароль result,
# для одного введённого числа.

# number = int(input("Введите число  от 3 до 20: "))
# list_check = []
# for i in range(3, number):
#     if number % i == 0:
#        for t in range(1, i):
#            # for r in range(1, t+1):
#             if t != (i - t):
#                 my_list = []
#                 pairNumbersOne = t
#                 pairNumbersTwo = (i - t)
#                 for j in range(1):
#                     my_list.append(pairNumbersOne)
#                     my_list.append(pairNumbersTwo)
#                 list_check.append(my_list)
#
# for e in range(1, number):
#     if e != (number - e):
#         my_list = []
#         pairNumbersOne = e
#         pairNumbersTwo = (number - e)
#         for j in range(1):
#             my_list.append(pairNumbersOne)
#             my_list.append(pairNumbersTwo)
#             list_check.append(my_list)
#
# result = []
# for h in range(len(list_check)):
#     list_ = []
#     list_.extend(list_check[h])
#     revers_list_check = list_[::-1]
#     if revers_list_check not in result:
#         result.append(list_check[h])
#
# result = (sorted(result))
# print(result)


def code_pairs(number):
    list_check = []
    for i in range(3, number):
        if number % i == 0:
            for t in range(1, i):
                if t != (i - t):
                    my_list = []
                    pairNumbersOne = t
                    pairNumbersTwo = (i - t)
                    for j in range(1):
                        my_list.append(pairNumbersOne)
                        my_list.append(pairNumbersTwo)
                    list_check.append(my_list)

    for e in range(1, number):
        if e != (number - e):
            my_list = []
            pairNumbersOne = e
            pairNumbersTwo = (number - e)
            for j in range(1):
                my_list.append(pairNumbersOne)
                my_list.append(pairNumbersTwo)
                list_check.append(my_list)
    return list_check


def sorting_by_uniqueness(list_check):
    result = []
    for h in range(len(list_check)):
        list_ = []
        list_.extend(list_check[h])
        revers_list_check = list_[::-1]
        if revers_list_check not in result:
            result.append(list_check[h])
    return result


def cod(numbers):
    result = sorted(sorting_by_uniqueness(code_pairs(numbers)))
    str_result = ""
    for i in result:
        for j in i:
            str_result = str_result + str(j)
    print(str_result)


number = int(input("Введите число  от 3 до 20: "))
cod(number)
