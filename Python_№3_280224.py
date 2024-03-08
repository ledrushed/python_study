# 1. Вывести на экран числа 100, 96, 92, ... до последнего положительного включительно.

for number in range(100, 0, -4):

    print(number)

# 2.Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8.

for i in range(12, 30, 2):

    print(i / 10)

# 3. Вывести на экран числа от 1000 до 9999 такие, что все цифры различны.

for num in range(1000, 10000):
    digits = [0] * 10
    is_unique = True
    for digit in str(num):
        if digits[int(digit)] == 1:
            is_unique = False
            break
        digits[int(digit)] = 1
    if is_unique:
        print(num)

# 4. Вывести на экран числа от 1000 до 9999 такие, что среди цифр нет цифр 5 и цифры 6.

for num in range(1000, 10000):
    if '5' not in str(num) and '6' not in str(num):
        print(num)

# 5. Вывести все пятизначные числа, которые делятся на 2, у которых средняя цифра нечетная, и сумма всех цифр делится на 4.

for num in range(10000, 100000):
    digits = [int(d) for d in str(num)]

    if num % 2 == 0 and digits[2] % 2 != 0 and sum(digits) % 4 == 0:
        print(num)

# 6. Вывести на экран числа от 1000 до 9999 такие, что среди цифр есть цифра 3.

for num in range(1000, 10000):
    if '3' in str(num):
        print(num)

# 7. Найдите трехзначные числа, равные сумме кубов своих цифр.

for num in range(100, 1000):
    digits = [int(digit) for digit in str(num)]

    sum_of_cubes = 0
    for digit in digits:
        sum_of_cubes += digit ** 3

    if num == sum_of_cubes:
        print(num)

# 8.Сколько существует четырехзначных чисел, которые в 600 раз больше суммы своих цифр?

count = 0

for num in range(1000, 10000):
    digits_sum = sum(int(digit) for digit in str(num))
    if num == 600 * digits_sum:
        count += 1

print(f"Количество четырехзначных чисел, удовлетворяющих условию: {count}")

# 9. Выведите на экран строки (в последней строке n звездочек):

# *
# **
# ***
# ****
# *****

n = 5

for i in range(1, n+1):
    print('*' * i)

# 10. Выведите на экран строки вида:

# *******
# ****
# *******
# ****
# *******
# ****

# (всего n строк, звездочек или 7, или 4 по очереди)

n = 7

for i in range(1, n+1):
    if i % 2 == 1:
        print('*' * 7)
    else:
        print('*' * 4)