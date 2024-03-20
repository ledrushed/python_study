# 1) Дан текст. Найти сумму имеющихся в нем цифр.

text = "Sample text with numbers 12345"

sum_digits = 0
for char in text:
    if char.isdigit():
        digit = int(char)
        sum_digits += digit

print("Sum of digits in the text:", sum_digits)


# 2) Дана строка. Заменить все символы 'a' и 'b' на 'A' и 'B' соответственно.

input_string = "This is an example with letter 'a' and 'b'."
replaced_string = ''

for char in input_string:
    if char == 'a':
        replaced_string += 'A'
    elif char == 'b':
        replaced_string += 'B'
    else:
        replaced_string += char

print(replaced_string)


# 3) # Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

input_string = "Это пример строки со словами разделенными пробелами"
word_count = input_string.count(' ') + 1

print("Количество слов в строке: ", word_count)

# 4) # Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.

input_string = "Первое Второе"
words = input_string.split()
reversed_string = ' '.join(reversed(words))

print("Строка после перестановки слов:", reversed_string)

# 5)  Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.

input_string = "abcdehfghi"
first_h = input_string.find('h')
last_h = input_string.rfind('h')

prefix = input_string[:first_h+1]
suffix = input_string[last_h:]
middle = input_string[first_h+1:last_h][::-1]

result_string = prefix + middle + suffix

print("Результат после разворота:", result_string)

# 6) Определить, является ли строка палиндромом. Палиндром – это число, слово или фраза, одинаково читающиеся в обоих направления.

input_string = "А роза упала на лапу Азора"
input_string = input_string.lower().replace(" ", "")

if input_string == input_string[::-1]:
    print(f"Строка '{input_string}' является палиндромом!")
else:
    print(f"Строка '{input_string}' не является палиндромом.")


# 7) Дана строка, состоящая из английских слов, разделенных пробелами и знаками препинания. Определить длину самого короткого слова.

input_string = "Hello, world! This is a test string."
words = input_string.split()
min_length = len(input_string)  # Предполагаем, что самое короткое слово длиннее всей строки

for word in words:
    cleaned_word = "".join(filter(str.isalnum, word))  # Удаляем знаки препинания
    if cleaned_word:  # Проверяем, что слово не пустое после удаления знаков препинания
        if len(cleaned_word) < min_length:  # Если длина очищенного слова меньше текущей минимальной
            min_length = len(cleaned_word)  # Обновляем минимальную длину

print(f"Длина самого короткого слова в строке: {min_length}")

# 8) Дана строка. Определите общее количество символов '+' и '-' в ней.

input_string = "This is a test string with + and - characters."
count_plus = 0
count_minus = 0

for char in input_string:
    if char == '+':
        count_plus += 1
    elif char == '-':
        count_minus += 1

total_count = count_plus + count_minus

print(f"Количество символов '+' в строке: {count_plus}")
print(f"Количество символов '-' в строке: {count_minus}")
print(f"Общее количество знаков '+' и '-' в строке: {total_count}")

# 9) # Дана строка. Вывести первые три символа и последние три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.

input_string = "abcdefg"

if len(input_string) > 5:
    first_three = input_string[:3]
    last_three = input_string[-3:]
    print(f"Первые три символа: {first_three}")
    print(f"Последние три символа: {last_three}")
else:
    first_character = input_string[0]
    repeated_character = first_character * len(input_string)
    print(f"Первый символ '{first_character}' повторен {len(input_string)} раз: {repeated_character}")


# 10) # Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.

input_string = "abcdefghwijklmnopqxrsuvwxyz"

if 'x' not in input_string or 'w' not in input_string:
    if 'x' not in input_string and 'w' not in input_string:
        print("Символы 'x' и 'w' отсутствуют в строке.")
    elif 'x' not in input_string:
        print("Символ 'x' отсутствует в строке.")
    else:
        print("Символ 'w' отсутствует в строке.")
else:
    if input_string.index('x') < input_string.index('w'):
        print("'x' встречается раньше чем 'w' в строке.")
    else:
        print("'w' встречается раньше чем 'x' в строке.")


# 11) # Даны две строки. Вывести большую по длине строку столько раз, на сколько символов отличаются строки.

string1 = "Python"
string2 = "JavaScript"

diff = abs(len(string1) - len(string2))

if len(string1) > len(string2):
    print(string1 * diff)
elif len(string1) < len(string2):
    print(string2 * diff)
else:
    print("Строки одинаковой длины.")

