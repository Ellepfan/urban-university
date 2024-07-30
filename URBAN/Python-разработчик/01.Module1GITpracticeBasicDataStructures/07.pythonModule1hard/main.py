# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать
# вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где
# ключом будет имя ученика, а значением - его средний балл.

my_dict = {}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
my_dict.update({students[0]:(sum(grades[0])) / (len(grades[0])),
                students[1]:(sum(grades[1])) / (len(grades[1])),
                students[2]:(sum(grades[2])) / (len(grades[2])),
                students[3]:(sum(grades[3])) / (len(grades[3])),
                students[4]:(sum(grades[4])) / (len(grades[4]))})
print(my_dict)
print()

my_dict_ = {}
i = 0
for i in range(len(grades)):
    my_dict_.update({students[i]:(sum(grades[i])) / (len(grades[i]))})
print(my_dict_)
