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

number = int(input("Введите число  от 3 до 20: "))
result = []
for i in range(3, number + 1):
    if number % i == 0:
        for multiple_number in range(1, i):
            if multiple_number != (i - multiple_number):
                my_list = []
                for j in range(1):
                    my_list.append(multiple_number)
                    my_list.append(i - multiple_number)
                revers_my_list = my_list[::-1]
                if revers_my_list not in result:
                    result.append(my_list)
result = sorted(result)
str_result = ""
for i in result:
    for j in i:
        str_result = str_result + str(j)
print(str_result)
