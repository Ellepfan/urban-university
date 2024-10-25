# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        for f in file.readlines():
            if  len(f)>1:
                all_data.append(f)
            else:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()

for i in filenames:
    read_info(i)

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения: {execution_time} секунд")

if __name__ == '__main__':
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Время выполнения: {execution_time} секунд")