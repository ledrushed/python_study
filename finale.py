from datetime import datetime
import re

# Программа будет записывать и хранить в словаре данные о записи на техническое обслуживание автомобиля
appointments = {}


def load_archive():
    try:
        with open("archive.txt", "r", encoding='utf-8') as file:
            for line in file:
                date_time, client_name, car_info = line.strip().split(',')
                appointments[date_time] = {'client_name': client_name, 'car_info': car_info}
    except FileNotFoundError:
        print("Файл архива не найден. Создан новый архив.")


def save_to_archive():
    with open("archive.txt", "w", encoding='utf-8') as file:
        for date_time, appointment_data in appointments.items():
            client_name = appointment_data['client_name']
            car_info = appointment_data['car_info']
            file.write(f"{date_time},{client_name},{car_info}\n")


def start():
    print("Добро пожаловать в программу записи на сервисное обслуживание автомобилей.\n\n")
    load_archive()
    user_menu()


# Запрашивает марку автомобиля и государственный номер в согласно паттерну '^[A-Z]\d{3}[A-Z]{2}\d{2,3}$'
def get_car_info():
    while True:
        car_brand = input("Введите марку автомобиля: ")
        car_number = input("Введите государственный номер автомобиля в формате 'A123AA78': ")

        # Проверяем формат государственного номера автомобиля
        if re.match(r'^[A-Za-zА-Яа-я]\d{3}[A-Za-zА-Яа-я]{2}\d{2,3}$', car_number):
            return f"{car_brand} - {car_number}"
        else:
            print("Ошибка! Неверный формат государственного номера. Пожалуйста, введите номер в формате 'A123AA78'.")


# Запрашивает Имя и Фамилию и возвращает в формате {name} {lastname}, так же проверяет на соответствие паттерну
def request_valid_name_lastname():
    name = input("Введите имя: ")
    while not re.match("^[A-Za-zА-Яа-я]+$", name):
        print("Некорректный ввод. Имя должно содержать только буквы.")
        name = input("Введите имя: ")

    lastname = input("Введите фамилию: ")
    while not re.match("^[A-Za-zА-Яа-я]+$", lastname):
        print("Некорректный ввод. Фамилия должна содержать только буквы.")
        lastname = input("Введите фамилию: ")
    rst = f"{name} {lastname}"
    return rst


# запрашивает число месяц и время, возвращает дате в формате '%H:%M %d.%m.%Y'
def date():
    while True:
        try:
            date_month = int(input("Введите желаемый месяц (1-12)\n>>> "))
            if date_month < 1 or date_month > 12:
                raise ValueError

            date_day = int(input("Введите желаемый день\n>>> "))
            if date_day < 1 or date_day > 31:
                raise ValueError

            date_time = input("Введите желаемое время в формате ЧЧ:ММ (например, 1130 для 11:30)\n>>> ")
            time = datetime.strptime(date_time, "%H%M")  # Принимаем время без двоеточия

            current_year = datetime.now().year
            formatted_date_time = datetime(
                current_year, date_month,
                date_day,
                time.hour,
                time.minute).strftime('%H:%M %d.%m.%Y')
            return formatted_date_time
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректные значения.")


# check_availability(date_time) возвращает True, если указанное время date_time еще не занято в расписании
def check_availability(date_time):
    return date_time not in appointments


# make_appointment создаёт запись на прием и уведомляет о результатах операции.
def make_appointment(client_name, car_info, date_time):
    if check_availability(date_time):
        appointments[date_time] = {'client_name': client_name, 'car_info': car_info}
        save_to_archive()
        print(f"\nЗапись для {client_name} на {date_time} успешно создана.\n")
    else:
        print("Извините, это время уже занято. Выберите другое время.")
# cancel_appointment отменяет запись на прием и уведомляет о результатах операции.
def cancel_appointment(date_time):
    if date_time in appointments:
        del appointments[date_time]
        save_to_archive()
        print(f"\nЗапись на {date_time} успешно отменена.\n")
    else:
        print("Не найдено записи на указанное время.")


def display_schedule(apps):
    if not apps:
        print(f"-------------------------------------------\n"
              f"Архив записей пуст\n"
              f"-------------------------------------------\n")
    else:
        print("Расписание технического обслуживания:\n")
        for date_time, appointment_data in apps.items():
            client_name = appointment_data['client_name']
            car_info = appointment_data['car_info']
            print(f"-------------------------------------------\n"
                  f"Дата: {date_time}\n"
                  f"Клиент: {client_name}\n"
                  f"Автомобиль: {car_info}\n"
                  f"-------------------------------------------\n")


def user_menu():
    answer = 0
    while answer != 5:
        try:
            if answer == 0:
                answer = int(input("Меню:\n"
                                   "1. Записаться на сервисное обслуживание автомобиля\n"
                                   "2. Проверить свободно ли время для записи\n"
                                   "3. Вывести все имеющиеся записи\n"
                                   "4. Отменить запись\n"
                                   "5. Закрыть программу\n"
                                   ">>> "))
            if answer == 1:
                print("\nВы выбрали:\n"
                      "1. Записаться на сервисное обслуживание автомобиля\n")
                client_name = request_valid_name_lastname()
                date_time = date()
                car_info = get_car_info()
                make_appointment(client_name, car_info, date_time)
                answer = 0
            elif answer == 2:
                print("\nВы выбрали:\n"
                      "2. Проверить свободно ли время для записи\n")
                date_time = date()
                if check_availability(date_time):
                    print("Время свободно, хотите записаться? Y/N\n")
                    inp = input(">>> ")
                    if inp == 'Y' or 'y':
                        answer = 1
                    else:
                        answer = 0
                else:
                    print("К сожалению, время занято, попробуете другое время? Y/N\n")
                    inp = input(">>> ")
                    if inp == 'Y' or 'y':
                        answer = 2
                    else:
                        answer = 0
            elif answer == 3:
                print("3. Вывести все имеющиеся записи\n")
                display_schedule(appointments)
                answer = 0
            elif answer == 4:
                print("4. Отменить запись\n")
                date_time = date()
                cancel_appointment(date_time)
                answer = 0
            elif answer == 5:
                print("5. Закрыть программу\n")
                print(">>> Работа программы завершена <<<\n")
                answer = 5
            else:
                print("\nВведите пожалуйста только целое число от 1 до 5 (согласно меню программы).\n")
                answer = 0
        except ValueError:
            print("\nВведите пожалуйста только целое число от 1 до 5 (согласно меню программы).\n")
            answer = 0
            continue


start()