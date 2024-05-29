# 1) Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования. Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате. Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата. На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов.
# В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов. Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. Участников нужно выводить в алфавитном порядке.
# вход
# 5
# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1
# выход
# McCain 16
# Obama 17
from collections import defaultdict

# Создаем словарь, чтобы хранить общее количество голосов для каждого кандидата
results = defaultdict(int)

# Считываем количество записей
n = int(input())

# Обрабатываем каждую запись
for _ in range(n):
    candidate, votes = input().split()
    results[candidate] += int(votes)

# Выводим результаты выборов в алфавитном порядке
for candidate in sorted(results.keys()):
    print(f"{candidate} {results[candidate]}")

# 2) Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# вход
# 1
# apple orange banana banana orange
# выход
# banana

from collections import Counter

# Считываем количество строк
n = int(input())

# Создаем счетчик для подсчета слов
word_counter = Counter()

# Обрабатываем каждую строку
for _ in range(n):
    words = input().split()
    word_counter.update(words)

# Находим самое часто встречающееся слово
most_common_words = word_counter.most_common()
max_count = most_common_words[0][1]
result = sorted([word for word, count in most_common_words if count == max_count])[0]

print(result)


# 3) В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. Для каждого файла известно, с какими действиями можно к нему обращаться:
# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же файлу может быть применено любое колличество запросов.
# Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.
# вход
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# выход
# OK
# Access denied
# Access denied
# OK
# OK

# Считываем число файлов и их права доступа
n = int(input())
files = {}

for _ in range(n):
    file, *permissions = input().split()
    files[file] = set(permissions)

# Считываем число запросов
m = int(input())

# Обрабатываем запросы
for _ in range(m):
    action, file = input().split()
    if action == 'read' and 'R' in files[file]:
        print('OK')
    elif action == 'write' and 'W' in files[file]:
        print('OK')
    elif action == 'execute' and 'X' in files[file]:
        print('OK')
    else:
        print('Access denied')

# 4) Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче.
#
# вход
# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
#
# выход
#
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

from collections import Counter

# Чтение входных данных
n = int(input())
words = [input().split() for _ in range(n)]

# Создание словаря слов
word_count = Counter(word for line in words for word in line)

# Сортировка по убыванию количества появления и лексикографическому порядку
sorted_words = sorted(word_count, key=lambda x: (-word_count[x], x))

# Вывод отсортированных слов
for word in sorted_words:
    print(word)


# 5) Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
#
# вход
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# выход
# Ukraine
# Russia
# Russia

# Чтение входных данных
n = int(input())
countries = {}
for _ in range(n):
    country, *cities = input().split()
    for city in cities:
        countries[city] = country

m = int(input())
cities_to_find = [input() for _ in range(m)]

# Поиск и вывод стран для каждого города
for city in cities_to_find:
    if city in countries:
        print(countries[city])


# 6) Однажды, разбирая старые книги на чердаке, школьник Вася нашёл англо-латинский словарь. Английский он к тому времени знал в совершенстве, и его мечтой было изучить латынь. Поэтому попавшийся словарь был как раз кстати.
# К сожалению, для полноценного изучения языка недостаточно только одного словаря: кроме англо-латинского необходим латинско-английский. За неимением лучшего он решил сделать второй словарь из первого.
# Как известно, словарь состоит из переводимых слов, к каждому из которых приводится несколько слов-переводов. Для каждого латинского слова, встречающегося где-либо в словаре, Вася предлагает найти все его переводы (то есть все английские слова, для которых наше латинское встречалось в его списке переводов), и считать их и только их переводами этого латинского слова.
# Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.
# В первой строке содержится единственное целое число N — количество английских слов в словаре. Далее следует N описаний. Каждое описание содержится в отдельной строке, в которой записано сначала английское слово, затем отделённый пробелами дефис, затем разделённые запятыми с пробелами переводы этого английского слова на латинский. Все слова состоят только из маленьких латинских букв. Переводы отсортированы в лексикографическом порядке. Порядок следования английских слов в словаре также лексикографический.
# Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных. В частности, первым должен идти перевод лексикографически минимального латинского слова, далее — второго в этом порядке и т.д. Внутри перевода английские слова должны быть также отсортированы лексикографически.
# вход
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# выход
# 7
# baca - fruit
# bacca - fruit
# malum - apple, punishment
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit

# Чтение входных данных
n = int(input())
latin_to_english = {}
for _ in range(n):
    english_word, translations = input().split(" - ")
    translations = translations.split(", ")
    for latin_word in translations:
        if latin_word not in latin_to_english:
            latin_to_english[latin_word] = []
        latin_to_english[latin_word].append(english_word)

# Формирование латинско-английского словаря
output = []
for latin_word in sorted(latin_to_english.keys()):
    english_translations = sorted(latin_to_english[latin_word])
    output.append(f"{latin_word} - {', '.join(english_translations)}")

# Вывод результата
print(len(output))
for line in output:
    print(line)

# 7) Учительница задала Пете домашнее задание — в заданном тексте расставить ударения в словах, после чего поручила Васе проверить это домашнее задание. Вася очень плохо знаком с данной темой, поэтому он нашел словарь, в котором указано, как ставятся ударения в словах. К сожалению, в этом словаре присутствуют не все слова. Вася решил, что в словах, которых нет в словаре, он будет считать, что Петя поставил ударения правильно, если в этом слове Петей поставлено ровно одно ударение.
# Оказалось, что в некоторых словах ударение может быть поставлено больше, чем одним способом. Вася решил, что в этом случае если то, как Петя поставил ударение, соответствует одному из приведенных в словаре вариантов, он будет засчитывать это как правильную расстановку ударения, а если не соответствует, то как ошибку.
# Вам дан словарь, которым пользовался Вася и домашнее задание, сданное Петей. Ваша задача — определить количество ошибок, которое в этом задании насчитает Вася.
# Вводится сначала число N — количество слов в словаре.
# Далее идет N строк со словами из словаря. Каждое слово состоит не более чем из 30 символов. Все слова состоят из маленьких и заглавных латинских букв. В каждом слове заглавная ровно одна буква — та, на которую попадает ударение. Слова в словаре расположены в алфавитном порядке. Если есть несколько возможностей расстановки ударения в одном и том же слове, то эти варианты в словаре идут в произвольном порядке.
# Далее идет упражнение, выполненное Петей. Упражнение представляет собой строку текста, суммарным объемом не более 300000 символов. Строка состоит из слов, которые разделяются между собой ровно одним пробелом. Длина каждого слова не превышает 30 символов. Все слова состоят из маленьких и заглавных латинских букв (заглавными обозначены те буквы, над которыми Петя поставил ударение). Петя мог по ошибке в каком-то слове поставить более одного ударения или не поставить ударения вовсе.
# Выведите количество ошибок в Петином тексте, которые найдет Вася.
# Примечания к примерам тестов
# 1. В слове cannot, согласно словарю возможно два варианта расстановки ударения. Эти варианты в словаре могут быть перечислены в любом порядке (т.е. как сначала cAnnot, а потом cannOt, так и наоборот). Две ошибки, совершенные Петей — это слова be (ударение вообще не поставлено) и fouNd (ударение поставлено неверно). Слово thE отсутствует в словаре, но поскольку в нем Петя поставил ровно одно ударение, признается верным.
# 2. Неверно расставлены ударения во всех словах, кроме The (оно отсутствует в словаре, в нем поставлено ровно одно ударение). В остальных словах либо ударные все буквы (в слове PAGE), либо не поставлено ни одного ударения.
#
# вход
# 4
# cAnnot
# cannOt
# fOund
# pAge
# thE pAge cAnnot be found
# выход
# 2

# Чтение входных данных
n = int(input())
accent_dict = {}
for _ in range(n):
    word = input().strip()
    accent_dict[word.lower()] = set([index for index, char in enumerate(word) if char.isupper()])

exercise = input().split()

# Подсчет ошибок
errors = 0
for word in exercise:
    word_lower = word.lower()
    if word_lower in accent_dict:
        accents = accent_dict[word_lower]
        if len(accents) != 1 or word_lower[accents.pop()] != word[accents.pop()]:
            errors += 1
    elif word_lower not in accent_dict:
        if sum([1 for char in word if char.isupper()]) != 1:
            errors += 1

print(errors)

# 8) Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
#
# вход
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5
# выход
# Ivanov:
# envelope 5
# marker 3
# paper 17
# Petrov:
# envelope 20
# pens 5

from collections import defaultdict

# Словарь для хранения покупок каждого покупателя
purchases = defaultdict(lambda: defaultdict(int))

# Чтение входных данных
while True:
    try:
        line = input().strip().split()
        if not line:
            break
        customer, item, quantity = line
        purchases[customer][item] += int(quantity)
    except EOFError:
        break

# Вывод результатов
for customer in sorted(purchases.keys()):
    print(customer + ":")
    for item in sorted(purchases[customer].keys()):
        print(item, purchases[customer][item])

# 9) В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента необходимо вывести его высоту.
# Примечание
# Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая сложности обращения к элементам словаря).
# вход
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# выход
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2

def calculate_heights(relationships):
    heights = {}

    # Функция для рекурсивного расчета высоты элемента
    def calculate_height(person):
        if person not in heights:
            heights[person] = 0
            if person in relationships:
                heights[person] = 1 + calculate_height(relationships[person])
        return heights[person]

    # Родоначальник
    root = None
    for child, parent in relationships.items():
        if parent not in relationships:
            root = parent
            break

    calculate_height(root)

    return heights


# Чтение входных данных
n = int(input())
relationships = {}
for _ in range(n - 1):
    child, parent = input().split()
    relationships[child] = parent

# Расчет высот элементов дерева
heights = calculate_heights(relationships)

# Вывод результатов
for person in sorted(heights.keys()):
    print(person, heights[person])

# 10) Даны два элемента в дереве. Определите, является ли один из них потомком другого.
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является предком первого или 0, если ни один из них не является предком другого.
#
# вход
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# 3
# Anna Nicholaus_I
# Peter_II Peter_I
# Alexei Paul_I
# выход
# 1 2 0

def is_ancestor(person1, person2, relationships):
    # Функция для проверки является ли person1 предком person2
    def is_ancestor_of(person1, person2):
        if person1 == person2:
            return True
        if person1 not in relationships:
            return False
        return is_ancestor_of(relationships[person1], person2)

    if is_ancestor_of(person1, person2):
        return 1
    elif is_ancestor_of(person2, person1):
        return 2
    else:
        return 0


# Чтение входных данных
n = int(input())
relationships = {}
for _ in range(n - 1):
    child, parent = input().split()
    relationships[child] = parent

# Чтение запросов
k = int(input())
for _ in range(k):
    person1, person2 = input().split()
    result = is_ancestor(person1, person2, relationships)
    print(result, end=' ')



