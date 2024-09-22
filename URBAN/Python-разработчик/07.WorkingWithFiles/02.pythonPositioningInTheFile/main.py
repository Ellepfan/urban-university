def custom_write(file_name, strings):
    strings_positions = {}
    count_lines = 0
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file_tell = file.tell()
        file.write(i + '\n')
        count_lines += 1
        strings_positions[count_lines, file_tell] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
