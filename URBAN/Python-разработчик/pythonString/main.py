example = "Первопроходец"

print("Выведите на экран(в консоль) первый символ этой строки. \n" , example[:1])
print("Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).\n", example[-1:])
print("Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').")c
print(example[int((len(example)-1)/2):])
print("Выведите на экран(в консоль) это слово наоборот.\n" ,example[::-1])

print("Выведите на экран(в консоль) каждый второй символ этой строкcdcи. (Пример: 'Топинамбур'->'оиабр')\n", example[1::2])