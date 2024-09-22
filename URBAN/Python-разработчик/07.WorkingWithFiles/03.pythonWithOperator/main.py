class WordsFinder:
    def __init__(self, *file_names):
        self.list_file_names = []
        for i in file_names:
            self.list_file_names.append(i)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for i in self.list_file_names:
            with open(i, encoding='utf-8') as file:
                lines = file.read()
                lines = lines.lower()
                for char in punctuation:
                    lines = lines.replace(char, '')
                all_words[i] = lines.split()
        return all_words

    def find(self, word):
        find = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            for count_word in enumerate(words):
                if word in count_word:
                    count_word = count_word[0] + 1
                    find[name] = count_word
                    break
        return find

    def count(self, word):
        count = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count_word_check = 0
            for i in words:
                if word in i:
                    count_word_check += 1
            count[name] = count_word_check
        return count

print('test_file.txt')
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print()
print('Mother Goose - Monday’s Child.txt')
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

print()
print('Rudyard Kipling - If.txt')
finder1 = WordsFinder('Rudyard Kipling - If.txt', )
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

print()
print('Walt Whitman - O Captain! My Captain!.txt')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

print()
print('ALL')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print()
print('find')
print(finder1.find('the'))
print()
print('count')
print(finder1.count('the'))
