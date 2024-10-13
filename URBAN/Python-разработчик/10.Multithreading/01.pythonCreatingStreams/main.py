from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово №{i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()
print(f"{time_end - time_start}")

time_start = datetime.now()
thr1 = Thread(target=write_words, args=(10, "example5.txt"))
thr2 = Thread(target=write_words, args=(30, "example6.txt"))
thr3 = Thread(target=write_words, args=(200, "example7.txt"))
thr4 = Thread(target=write_words, args=(100, "example8.txt"))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()
time_end = datetime.now()
print(f"{time_end - time_start}")
