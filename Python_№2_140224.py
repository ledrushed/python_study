# 01. Дано трехзначное число. Найдите сумму его цифр
def sum_of_digits(number):
    digit1 = number // 100
    digit2 = (number // 10) % 10
    digit3 = number % 10
    sum_digits = digit1 + digit2 + digit3
    return sum_digits

number = int(input("Введите трехзначное число: "))
result = sum_of_digits(number)

print("Сумма цифр введенного числа:", result)

# 02. Дано натуральное число. Требуется определить, является ли год с данным номером високосным.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Введите год: "))

if is_leap_year(year):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")

# 03. Решите квадратное уравнение с помощью коэф-ов a, b, c.

import cmath

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return x1, x2
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return x1, x2

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

solution = solve_quadratic_equation(a, b, c)

print("Решения квадратного уравнения:")
print("x1 =", solution[0])
print("x2 =", solution[1])

# 04. Пользователь вводит номер месяца. Вывести название поры года (весна, лето и т.д.)

def get_season(month):
    if month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "лето"
    elif month in [9, 10, 11]:
        return "осень"
    else:
        return "зима"

month_number = int(input("Введите номер месяца (от 1 до 12): "))

if month_number < 1 or month_number > 12:
    print("Неверный номер месяца. Введите число от 1 до 12.")
else:
    season = get_season(month_number)
    print(f"Пора года: {season}")

# 05. Даны три числа. Написать "yes", если среди них есть одинаковые, иначе "no"

def check_for_duplicates(num1, num2, num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "yes"
    else:
        return "no"

num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num3 = int(input("Третье число: "))

result = check_for_duplicates(num1, num2, num3)
print(result)

#06. Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию?
# Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.

def check_digits_decreasing(num):
    digits = [int(d) for d in str(num)]
    if digits == sorted(digits, reverse=True):
        return "Да, цифры расположены по убыванию."
    else:
        return "Нет, цифры не расположены по убыванию."

num = int(input("Введите четырехзначное число: "))

result = check_digits_decreasing(num)
print(result)

#07. Дано четырехзначное число. Если оно читается слева направо и справа налево одинаково, то вывести yes, иначе no.

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Введите четырехзначное число: "))

if is_palindrome(num):
    print("yes")
else:
    print("no")

#08. Дана дата из трех чисел (день, месяц и год). Вывести yes, если такая дата существует

def is_valid_date(day, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:
        return False

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

if is_valid_date(day, month, year):
    print("yes")
else:
    print("no")

#09. Проверить условие треугольника
# Если каждая сторона треугольника меньше суммы двух других сторон, значит треугольник существует
# Вывести Да или Нет

def is_triangle(side1, side2, side3):
    return (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2)

side1 = float(input("Введите длину первой стороны треугольника: "))
side2 = float(input("Введите длину второй стороны треугольника: "))
side3 = float(input("Введите длину третьей стороны треугольника: "))

if is_triangle(side1, side2, side3):
    print("Да")
else:
    print("Нет")

#10. Даны три числа. Найдите те два из них, сумма которых наибольшая
def find_max_sum_pair(num1, num2, num3):
    sum1 = num1 + num2
    sum2 = num1 + num3
    sum3 = num2 + num3

    max_sum = max(sum1, sum2, sum3)

    if max_sum == sum1:
        return num1, num2
    elif max_sum == sum2:
        return num1, num3
    else:
        return num2, num3


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

pair = find_max_sum_pair(num1, num2, num3)
print("Два числа, сумма которых наибольшая:", pair)