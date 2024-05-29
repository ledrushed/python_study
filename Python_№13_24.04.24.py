# Зачет в олимпиаде проводится без деления на классы. Выведите фамилию и имя победителя олимпиады. Если таких несколько - выведите только их количество.
# Примеры
# входные данные
# Иванов Сергей 9 90
# Сергеев Петр 10 95
# Петров Иван 11 85
# выходные данные
# Сергеев Петр
# входные данные
# Иванов Сергей 9 90
# Сергеев Петр 10 85
# Петров Иван 11 90
# выходные данные
# 2

# Создаем пустой словарь для хранения результатов участников олимпиады
participants = {}

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        name = ' '.join(data[:-2])
        score = int(data[-1])

        if score not in participants:
            participants[score] = [name]
        else:
            participants[score].append(name)

    except EOFError:
        break

# Находим максимальный балл
max_score = max(participants.keys())

# Проверяем, сколько участников набрали максимальный балл
winners = participants[max_score]

# Выводим результат
if len(winners) == 1:
    print(winners[0])
else:
    print(len(winners))

# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший балл среди всех участников в данном классе.
# Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.
# Выходные данные
# Выведите три целых числа.
# Примеры
# входные данные
# Иванов Сергей 9 80
# Сергеев Петр 10 82
# Петров Василий 11 82
# Васильев Андрей 9 81
# Андреев Александр 10 81
# Александров Роман 9 81
# Романов Иван 11 83
# выходные данные
# 80 81 82

# Создаем словарь для хранения максимальных баллов в каждом классе
max_scores = {}

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        class_num = int(data[-2])
        score = int(data[-1])

        if class_num not in max_scores or score > max_scores[class_num]:
            max_scores[class_num] = score

    except EOFError:
        break

# Сортируем баллы в порядке возрастания и выводим первые три максимальных балла
sorted_scores = sorted(max_scores.values())
print(sorted_scores[-3], sorted_scores[-2], sorted_scores[-1])

# Результаты олимпиады подводятся без деления на классы. Победителем олимпиады становятся те, кто набрал больше всего баллов. Призерами олимпиады становятся участники, следующие за победителями.
# Определите наибольший балл, который набрали призеры олимпиады и количество участников олимпиады, набравших такой балл.
# Выходные данные
# Выведите два числа: наибольший балл призера и количество участников, имеющий такой балл.
# Примеры
# входные данные
# Иванов Сергей 9 92
# Сергеев Петр 10 91
# Петров Василий 11 92
# Васильев Иван 9 93
# выходные данные
# 92 2

# Создаем список для хранения баллов всех участников
scores = []

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        score = int(data[-1])
        scores.append(score)

    except EOFError:
        break

# Сортируем баллы в порядке убывания
sorted_scores = sorted(scores, reverse=True)

# Находим балл призера
prize_score = sorted_scores[2]

# Находим количество участников с таким баллом
prize_count = 0
for score in sorted_scores:
    if score == prize_score:
        prize_count += 1
    else:
        break

print(prize_score, prize_count)


# В условиях предыдущей задачи выведите фамилию и имя участника олимпиады, набравшего наибольший балл, но не ставшего победителем. Если таких школьников несколько - выведите их количество.
# Примеры
# входные данные
# Иванов Сергей 9 93
# Сергеев Петр 10 91
# Петров Василий 11 92
# Васильев Иван 9 93
# выходные данные
# Петров Василий

# Создаем список для хранения данных о участниках олимпиады
participants = []

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        name = ' '.join(data[:-2])
        class_num = int(data[-2])
        score = int(data[-1])

        participants.append((name, score))

    except EOFError:
        break

# Сортируем участников по убыванию баллов
sorted_participants = sorted(participants, key=lambda x: x[1], reverse=True)

# Находим победителя олимпиады (участника с самым высоким баллом)
winner_score = sorted_participants[0][1]

# Находим первого призера, не ставшего победителем
runner_up = None
for name, score in sorted_participants[1:]:
    if score < winner_score:
        runner_up = name
        break

# Печатаем результат
if runner_up is not None:
    # Находим количество участников с баллом таким же как у первого призера
    runner_up_count = sum(1 for _, score in sorted_participants if score == sorted_participants[1][1])

    print(runner_up)
else:
    runner_up_count = 0
    print(runner_up_count)

# В олимпиаде по информатике принимало участие \(N\) человек. Определите школы, из которых в олимпиаде принимало участие больше всего участников. В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех участниках, а только подсчитывая число участников для каждой школы.
# Входные данные
# Информация о результатах олимпиады записана в файле, каждая из строк которого имеет вид:
# фамилия имя школа балл
# Фамилия и имя — текстовые строки, не содержащие пробелов. Школа — целое число от 1 до 99. Балл — целое число от 0 до 100.
# Выходные данные
# Выведите номера этих школ в порядке возрастания.
# Примеры
# входные данные
# Иванов Сергей 14 56
# Сергеев Петр 23 74
# Петров Василий 3 99
# Васильев Андрей 3 56
# Андреев Роман 14 75
# Романов Иван 27 68
# выходные данные
# 3 14

from collections import defaultdict

# Создаем словарь для хранения количества участников из каждой школы
school_participants = defaultdict(int)

# Считываем данные из файла построчно
with open('results.txt', 'r') as file:
    for line in file:
        data = line.split()
        school = int(data[2])
        school_participants[school] += 1

# Находим школы с максимальным количеством участников
max_participants = max(school_participants.values())
most_popular_schools = [school for school, participants in school_participants.items() if participants == max_participants]

# Выводим номера этих школ в порядке возрастания
most_popular_schools.sort()
print(' '.join(map(str, most_popular_schools)))

# В условиях предыдущей задачи определите школы, из которых в олимпиаде принимало участие меньше всего участников (но был хотя бы один участник).
# Выходные данные
# Выведите номера этих школ в порядке возрастания.
# Примеры
# входные данные
# Иванов Сергей 14 56
# Сергеев Петр 23 74
# Петров Василий 3 99
# Васильев Андрей 3 56
# Андреев Роман 14 75
# Романов Иван 27 68
# выходные данные
# 23 27

from collections import defaultdict

# Создаем словарь для хранения количества участников из каждой школы
school_participants = defaultdict(int)

# Считываем данные из файла построчно
with open('results.txt', 'r') as file:
    for line in file:
        data = line.split()
        school = int(data[2])
        school_participants[school] += 1

# Находим школы с минимальным количеством участников (но не равным 0)
min_participants = min(participants for participants in school_participants.values() if participants > 0)
least_popular_schools = [school for school, participants in school_participants.items() if participants == min_participants]

# Выводим номера этих школ в порядке возрастания
least_popular_schools.sort()
print(' '.join(map(str, least_popular_schools)))

# В условиях предыдущей задачи выведите в порядке возрастания номера школ, в которых есть хотя бы один победитель олимпиады.
# Примеры
# входные данные
# Иванов Сергей 13 80
# Сергеев Петр 26 70
# Сергеев Андрей 35 80
# Петров Василий 13 80
# Иванов Роман 35 70
# Иванов Иван 26 70
# выходные данные
# 13 35

from collections import defaultdict

# Создаем словарь для хранения информации о победителях в каждой школе
winners = defaultdict(int)

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        school = int(data[-2])
        score = int(data[-1])

        if score == max([int(entry.split()[-1]) for entry in winners if int(entry[-2]) == school], default=0):
            winners[f'{data[0]} {data[1]} {school}'] = score  # Записываем фамилию, имя и номер школы победителя
        else:
            if winners[f'{data[0]} {data[1]} {school}]:  # Если не победитель, удаляем из словаря
                del winners[f'{data[0]} {data[1]} {school}']

    except EOFError:
        break

# Извлекаем номера школ, в которых есть хотя бы один победитель олимпиады
schools_with_winners = sorted({int(entry.split()[-1]) for entry in winners})

# Выводим номера школ в порядке возрастания
print(' '.join(map(str, schools_with_winners)))

# 9)
# В условиях предыдущей задачи выведите в порядке возрастания номера школ, средний балл учащихся которых выше, чем средний балл всех участников олимпиады (то есть необходимо вычислить средний балл для каждой школы и средний балл по всем участникам).
# Примеры
# входные данные
# Иванов Сергей 13 80
# Сергеев Петр 26 70
# Сергеев Андрей 35 80
# Петров Василий 13 80
# Иванов Роман 35 70
# Иванов Иван 26 70
# выходные данные
# 13

from collections import defaultdict

# Создаем словарь для хранения суммы баллов и количества участников в каждой школе
school_scores = defaultdict(int)
school_counts = defaultdict(int)

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        school = int(data[-2])
        score = int(data[-1])

        school_scores[school] += score
        school_counts[school] += 1

    except EOFError:
        break

# Вычисляем средний балл для каждой школы
school_avg_scores = {school: school_scores[school] / school_counts[school] for school in school_scores}

# Вычисляем общий средний балл по всем участникам олимпиады
total_avg_score = sum(school_scores.values()) / sum(school_counts.values())

# Определяем номера школ, средний балл учащихся которых выше, чем общий средний балл
schools_above_avg = [school for school, avg_score in school_avg_scores.items() if avg_score > total_avg_score]

# Выводим номера таких школ в порядке возрастания
print(' '.join(map(str, sorted(schools_above_avg))))

10)
В условиях предыдущей задачи выведите в порядке возрастания номера школ, из которых наибольшее количество участников стало победителями олимпиады.
Примеры
входные данные
Иванов Сергей 13 70
Сергеев Петр 13 60
Сергеев Андрей 20 70
Петров Василий 20 70
Иванов Роман 70 60
Иванов Иван 70 60
выходные данные
20

# 10)
# В условиях предыдущей задачи выведите в порядке возрастания номера школ, из которых наибольшее количество участников стало победителями олимпиады.
# Примеры
# входные данные
# Иванов Сергей 13 70
# Сергеев Петр 13 60
# Сергеев Андрей 20 70
# Петров Василий 20 70
# Иванов Роман 70 60
# Иванов Иван 70 60
# выходные данные
# 20
#
from collections import defaultdict

# Создаем словарь для хранения количества победителей из каждой школы
winners_count = defaultdict(int)

# Создаем словарь для хранения количества участников из каждой школы
participants_count = defaultdict(int)

# Считываем данные об участниках олимпиады
while True:
    try:
        data = input().split()
        if not data:
            break

        school = int(data[-2])
        score = int(data[-1])

        participants_count[school] += 1

        if score == max([int(entry.split()[-1]) for entry in winners_count if int(entry.split()[-2]) == school], default=0):
            winners_count[f'{data[0]} {data[1]} {school}'] = score
        else:
            if winners_count[f'{data[0]} {data[1]} {school}']:
                del winners_count[f'{data[0]} {data[1]} {school}']

    except EOFError:
        break

# Находим номера школ, из которых наибольшее количество участников стало победителями олимпиады
max_winners_schools = [school for school in participants_count if participants_count[school] == winners_count.values().count(max(winners_count.values()))]

# Выводим номера таких школ в порядке возрастания
print(' '.join(map(str, sorted(max_winners_schools))))

