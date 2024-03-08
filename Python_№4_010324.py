# 01. Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

max_number = 0

while True:
    number = int(input("Введите число (Введите 0 для завершения): "))

    if number == 0:
        break

    if number > max_number:
        max_number = number

print("Наибольший элемент в последовательности:", max_number)

# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите индекс наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите индекс первого из них.
# Нумерация элементов начинается с нуля.

numbers = []
index = -1
max_number = float('-inf')

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)
    if num > max_number:
        max_number = num
        index = len(numbers) - 1

print(index)

# 3.Определите количество четных элементов в последовательности, завершающейся числом 0.

count_even = 0

while True:
    num = int(input("Введите число (для завершения введите 0): "))
    if num == 0:
        break
    if num % 2 == 0:
        count_even += 1

print(f"Количество четных элементов в последовательности: {count_even}")

# 4. Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

count_greater = 0
prev_num = None

while True:
    num = int(input("Введите натуральное число (для завершения введите 0): "))
    if num == 0:
        break
    if prev_num is not None and num > prev_num:
        count_greater += 1
    prev_num = num

print(f"Количество элементов больше предыдущего: {count_greater}")


# 5. Найдите количество целых чисел от a до b включительно, которые делятся на 12.

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

count_divisible_by_12 = 0

for num in range(a, b + 1):
    if num % 12 == 0:
        count_divisible_by_12 += 1

print(f"Количество целых чисел от {a} до {b}, которые делятся на 12: {count_divisible_by_12}")

# 6. Пользователь вводит ненулевые числа до тех пор пока не введет ноль. Найдите сумму этих чисел.

sum_of_numbers = 0

while True:
    num = float(input("Введите число (для выхода введите 0): "))

    if num == 0:
        break

    sum_of_numbers += num

print(f"Сумма введенных ненулевых чисел: {sum_of_numbers}")

# 7. Пользователь вводит ненулевые целые числа до тех пор, пока не введет ноль. Найдите количество четных чисел, которые он ввел.

count_even_numbers = 0

while True:
    num = int(input("Введите целое число (для выхода введите 0): "))

    if num == 0:
        break

    if num % 2 == 0:
        count_even_numbers += 1

print(f"Количество введенных четных чисел: {count_even_numbers}")

# 8. Найдите четырехзначные числа, сумма цифр которых равна 15.

for number in range(1000, 10000):
    digit_sum = sum(int(digit) for digit in str(number))

    if digit_sum == 15:
        print(number)

# 9. Найдите наибольшую цифру в данном натуральном числе.

number = input("Введите натуральное число: ")
max_digit = max(int(digit) for digit in number)
print(f"Наибольшая цифра в числе {number} - {max_digit}")

# 10. Дано натуральное число. Найдите количество четных цифр.

number = input("Введите натуральное число: ")
count_even_digits = sum(1 for digit in number if int(digit) % 2 == 0)
print(f"Количество четных цифр в числе {number}: {count_even_digits}")
