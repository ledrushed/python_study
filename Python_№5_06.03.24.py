#1) Два числа называются дружественными, если каждое из них равно сумме всех делителей второго не считая самого этого числа. Найдите все пары дружественных чисел на отрезке [a;b].

def sum_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def find_friendly_numbers(a, b):
    friendly_pairs = []
    for i in range(a, b+1):
        for j in range(i+1, b+1):
            if sum_divisors(i) == j and sum_divisors(j) == i:
                friendly_pairs.append((i, j))
    return friendly_pairs

a = 200
b = 300
friendly_pairs = find_friendly_numbers(a, b)
print("Пары дружественных чисел на отрезке [{}, {}]:".format(a, b))
for pair in friendly_pairs:
    print(pair)

#2) Натуральное число называется совершенным, если оно равно сумме всех своих делителей, не равных самому числу. Найдите все совершенные числа, меньшие данного натурального числа n.

def find_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n):
        divisors_sum = sum([j for j in range(1, i) if i % j == 0])
        if divisors_sum == i:
            perfect_numbers.append(i)
    return perfect_numbers

n = int(input("Введите натуральное число n: "))
perfect_numbers = find_perfect_numbers(n)
print(f"Совершенные числа, меньшие {n}: {perfect_numbers}")

#3) Назовем автобусный билет несчастливым, если сумма цифр его шестизначного номера делится на 13. Могут ли два идущих подряд билета оказаться несчастливыми?

def is_unlucky_ticket(ticket_number):
    return sum(map(int, str(ticket_number))) % 13 == 0

ticket1 = int(input("Введите номер первого билета (шестизначное число): "))
ticket2 = ticket1 + 1

if is_unlucky_ticket(ticket1) and is_unlucky_ticket(ticket2):
    print("Два идущих подряд билета могут оказаться несчастливыми. ")
else:
    print("Два идущих подряд билета не могут оказаться оба несчастливыми. ")


#4) Найдите, сколько точек с целочисленными координатами попадает в круг радиуса r  с центром в точке (x,y).

import math

def count_points_in_circle(x, y, r):
    count = 0
    for a in range(x - r, x + r + 1):
        for b in range(y - r, y + r + 1):
            if (x - a)**2 + (y - b)**2 <= r**2:
                count += 1
    return count

x = 0
y = 0
r = 5

result = count_points_in_circle(x, y, r)
print(f"Количество точек с целочисленными координатами, попавших в круг радиуса {r} с центром в точке ({x},{y}): {result}")

#5) Вывести ряд чисел: десять десяток, девять девяток, восемь восьмерок, ... , одну единицу.
#Найти сумму всех этих чисел.

def calculate_sum_of_series():
    total_sum = 0
    for i in range(10, 0, -1):
        current_number = int(str(i) * i)
        print(f"{i} раз: {current_number}")
        total_sum += current_number
    return total_sum

result = calculate_sum_of_series()
print(f"Сумма всех чисел в ряде: {result}")

#6) Из натурального числа удалить заданную цифру. Число и цифру вводить с клавиатуры.
#Например, задано число 5683. Требуется удалить из него цифру 8. Получится число 563.

def remove_digit_from_number(number, digit_to_remove):
    number_str = str(number)
    result_str = number_str.replace(str(digit_to_remove), "")
    result = int(result_str)
    return result

number = int(input("Введите натуральное число: "))
digit_to_remove = int(input("Введите цифру для удаления: "))

result = remove_digit_from_number(number, digit_to_remove)
print(f"Результат после удаления цифры {digit_to_remove}: {result}")

#7) Написать программу, в которой вводятся два числа-операнда x и y и знак арифметической операции (+, –, /, *). Вычислить результат z в зависимости от знака.
#Предусмотреть реакции на возможный неверный знак операции, а также на ввод y=0 при делении.
#Организовать возможность многократных вычислений без перезагрузки программы (то есть построить цикл). В качестве символа прекращения вычислений принять '0'.

while True:
    x = float(input("Введите первое число x: "))
    y = float(input("Введите второе число y: "))
    operation = input("Введите знак арифметической операции (+, -, /, *): ")

    if operation == '0':
        print("Программа завершена.")
        break

    if operation not in ['+', '-', '/', '*']:
        print("Неверный знак операции. Попробуйте снова.")
        continue

    if operation == '+':
        z = x + y
    elif operation == '-':
        z = x - y
    elif operation == '*':
        z = x * y
    else:
        if y == 0:
            print("Ошибка: деление на ноль.")
            continue
        z = x / y

    print(f"Результат: {z}\n")

#8) С клавиатуры вводятся целые числа до первого числа, которое меньше двух. Написать программу, которая определяет сколько простых чисел было введено.
#Простые числа - это натуральные числа больше единицы, которые делятся нацело только на единицу и на себя. Например, число 3 простое, так как нацело делится только на 1 и 3. Число 4 сложное, так как нацело делится не только на 1 и 4, но также на число 2.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


count_primes = 0

while True:
    num = int(input("Введите целое число: "))

    if num < 2:
        break

    if is_prime(num):
        count_primes += 1

print(f"Количество простых чисел, введенных до числа меньше двух: {count_primes}")

#9) Гипотеза Сиракуз: возьмем любое натуральное число. Если оно четное - разделим его пополам, если нечетное - умножим на 3, прибавим 1 и разделим пополам. Повторим эти действия с вновь полученным числом. Гипотеза гласит, что независимо от выбора первого числа рано или поздно мы получим 1.
#Проверить гипотезу Сиракуз для всех чисел от 20 до 30.

def syracuse_conjecture(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

for i in range(20, 31):
    sequence = syracuse_conjecture(i)
    print(f"Для числа {i}: {sequence}")


#10) Требуется вывести на экран двумерную таблицу умножения.
#Подобное реализуется с помощью двух циклов. При этом один цикл должен быть вложен в другой.

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")
    print()