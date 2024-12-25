import csv

class FinancialManagementSystem:
    def __init__(self, filename="finance_data.txt"):
        self.filename = filename
        self.records = self.load_data()

    def load_data(self):
        records = []
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                    if row:
                        category, amount, transaction_type = row
                        records.append({
                            "category": category,
                            "amount": float(amount),
                            "type": transaction_type
                        })
        except FileNotFoundError:
            pass  # File doesn't exist yet, so we'll just start with an empty list
        return records

    def save_data(self):
        with open(self.filename, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            for record in self.records:
                writer.writerow([record["category"], record["amount"], record["type"]])

    def add_record(self, category, amount, transaction_type):
        record = {
            "category": category,
            "amount": amount,
            "type": transaction_type
        }
        self.records.append(record)
        self.save_data()

    def show_records(self):
        if not self.records:
            print("Нет записей.")
            return
        for i, record in enumerate(self.records, 1):
            print(f"{i}. Категория: {record['category']}, Сумма: {record['amount']} ₽, Тип: {record['type']}")

    def get_balance(self):
        income = sum(record['amount'] for record in self.records if record['type'] == "доход")
        expense = sum(record['amount'] for record in self.records if record['type'] == "расход")
        return income - expense

    def export_data(self):
        export_filename = input("Введите имя файла для экспорта (например, 'export.csv'): ")
        try:
            with open(export_filename, mode="w", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(["Категория", "Сумма", "Тип"])
                for record in self.records:
                    writer.writerow([record["category"], record["amount"], record["type"]])
            print(f"Данные успешно экспортированы в файл: {export_filename}")
        except Exception as e:
            print(f"Ошибка при экспорте: {e}")

def main():
    print("Система управления финансами")
    system = FinancialManagementSystem()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Показать баланс")
        print("4. Экспортировать данные")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            category = input("Введите категорию: ")
            amount = float(input("Введите сумму: "))
            transaction_type = input("Введите тип (доход/расход): ").lower()

            if transaction_type not in ["доход", "расход"]:
                print("Некорректный тип. Попробуйте снова.")
                continue

            system.add_record(category, amount, transaction_type)
            print("Запись добавлена.")

        elif choice == "2":
            system.show_records()

        elif choice == "3":
            balance = system.get_balance()
            print(f"Текущий баланс: {balance} ₽")

        elif choice == "4":
            system.export_data()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
