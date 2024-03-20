# 1) Дан текст. Найти сумму имеющихся в нем цифр.

текст = "Текст с 123 цифрами 456 для примера 789"  # ваш текст
сумма_цифр = 0

for символ in текст:
    if символ.isdigit():
        сумма_цифр += int(символ)

print("Сумма цифр в тексте равна:", сумма_цифр)


# 2) Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно.

def заменить_символы(string):
    string_измененная = string.replace('a', 'A').replace('b', 'B')
    return string_измененная

исходная_строка = input("Введите строку: ")
измененная_строка = заменить_символы(исходная_строка)
print(f"Исходная строка: {исходная_строка}")
print(f"Измененная строка: {измененная_строка}")

# 3) # Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

строка = input("Введите строку: ")
количество_слов = строка.count(' ') + 1
print(f"Количество слов в строке: {количество_слов}")

# 4) # Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.

строка = "Первое Второе"

слова = строка.split()
переставленная_строка = слова[1] + " " + слова[0]

print("Переставленные слова:", переставленная_строка)

строка = "Первое Второе"

слова = строка.split()
переставленная_строка = слова[1] + " " + слова[0]

print("Переставленные слова:", переставленная_строка)

# 5)  Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

строка = "abcdefhghi"  # Пример строки

первое_вхождение = строка.find('h')
последнее_вхождение = строка.rfind('h')

между_h = строка[первое_вхождение + 1 : последнее_вхождение]

развернутая_последовательность = строка[:первое_вхождение + 1] + между_h[::-1] + строка[последнее_вхождение:]

print("Результат разворота между 'h':", развернутая_последовательность)

# 6) Определить, является ли строка палиндромом. Палиндром – это число, слово или фраза, одинаково читающиеся в обоих направления.

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

строка = "А роза упала на лапу Азора"

if is_palindrome(строка):
    print("Данная строка является палиндромом.")
else:
    print("Данная строка не является палиндромом.")

# 7) Дана строка, состоящая из английских слов, разделенных пробелами и знаками препинания. Определить длину самого короткого слова.

def find_shortest_word_length_no_inf(s):
    words = s.split()
    shortest_word_length = None

    for word in words:
        clean_word = ''.join(filter(str.isalpha, word))
        word_length = len(clean_word)

        if clean_word and (shortest_word_length is None or word_length < shortest_word_length):
            shortest_word_length = word_length

    return shortest_word_length if shortest_word_length is not None else 0

string = "According to Marx, escalating tension between the upper and lower class is a major consequence of technology decreasing the value of labor force and the contradictory effect an evolving means of production has on established social and economic systems"
print(find_shortest_word_length_no_inf(string))

# 8) Дана строка. Определите общее количество символов '+' и '-' в ней.

def count_plus_minus_chars(s):
    count_plus = 0
    count_minus = 0

    for char in s:
        if char == '+':
            count_plus += 1
        elif char == '-':
            count_minus += 1

    return count_plus, count_minus

string = "++--Hello-+World--+"
count_plus, count_minus = count_plus_minus_chars(string)
print("Количество символов '+' в строке:", count_plus)
print("Количество символов '-' в строке:", count_minus)

def first_and_last_three_chars(s):
    if len(s) > 5:
        first_three = s[:3]
        last_three = s[-3:]
        return first_three, last_three
    else:
        return "Длина строки меньше или равна 5 символам."

# 9) # Дана строка. Вывести первые три символа и последние три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.
def process_string(s):
    if len(s) > 5:
        return s[:3] + s[-3:]
    else:
        return s[0] * len(s)

input_string = "Determinant"
output = process_string(input_string)

print(output)

# 10) # Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.

def find_earlier_char(s):
    if 'x' not in s and 'w' not in s:
        return "В строке нет символов 'x' и 'w'."
    elif 'x' not in s:
        return "'w' встречается раньше символа 'x'."
    elif 'w' not in s:
        return "'x' встречается раньше символа 'w'."
    else:
        index_x = s.index('x')
        index_w = s.index('w')
        if index_x < index_w:
            return "'x' встречается раньше символа 'w'."
        else:
            return "'w' встречается раньше символа 'x'."

input_string = "ahdwxcy"
output = find_earlier_char(input_string)

print(output)

# 11) # Даны две строки. Вывести большую по длине строку столько раз, на сколько символов отличаются строки.

def print_string_difference(str1, str2):
    if len(str1) > len(str2):
        print(str1 * (len(str1) - len(str2)))
    elif len(str2) > len(str1):
        print(str2 * (len(str2) - len(str1)))

string1 = "Example"
string2 = "Example1"
print_string_difference(string1, string2)
