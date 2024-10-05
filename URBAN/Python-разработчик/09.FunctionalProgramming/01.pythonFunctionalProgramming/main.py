# Задача "Вызов разом":
# Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам,
# состоящим из чисел)
# Эта функция должна:
# Вызвать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции,
# а значением - её результат работы со списком int_list.

def apply_all_func(int_list, *functions):
    results_ditc = {}
    for my_functions in functions:
        result = my_functions(int_list)
        name = my_functions.__name__
        results_ditc[name] = result
    return results_ditc


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
