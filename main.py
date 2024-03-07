from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)  # Створення об'єкта класу Name
        self.phones = []  # Ініціалізація списку телефонів

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # Додавання об'єкта Phone до списку

    def edit_phone(self, old_phone, new_phone):
        for phone_obj in self.phones:
            if str(phone_obj) == old_phone and Phone(new_phone):  # Пошук старого номера телефону
                index = self.phones.index(phone_obj)
                self.phones.pop(index)  # Видалення старого номера телефону
                self.phones.insert(index, Phone(new_phone))  # Вставка нового номера телефону
                return
        raise ValueError  # Вивід повідомлення про помилку, якщо номер не знайдено

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if str(phone_obj) == phone:  # Пошук номера телефону
                return phone

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if str(phone_obj) == phone:  # Пошук і видалення номера телефону
                self.phones.remove(phone_obj)

    def __str__(self):
        return f"Контакт: {self.name.value}, телефони: {'; '.join(p.value for p in self.phones)}"  # Форматування рядка виводу


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}  # Ініціалізація словника даних
        self.obj_data = {}  # Ініціалізація словника об'єктів

    # реалізація класу
    def add_record(self, record: Record):
        self.data[str(record.name)] = [str(phone) for phone in record.phones]  # Додавання запису до даних
        self.obj_data[str(record.name)] = record  # Додавання запису до словника об'єктів

    def find(self, name):
        return self.obj_data.get(name)  # Пошук запису за ім'ям

    def delete(self, name):
        if name in self.data:
            del self.data[name]  # Видалення запису з даних
            del self.obj_data[name]  # Видалення запису з словника об'єктів
        else:
            print('NotFound')  # Вивід повідомлення про помилку, якщо запис не знайдено


def main():
    book = AddressBook()

    john_record = Record('John')
    john_record.add_phone('1234567890')
    john_record.add_phone('5555555555')

    book.add_record(john_record)

    jane_record = Record('Jane')
    jane_record.add_phone('9876543210')
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(f'{name}: {record}')

    john = book.find('John')
    john.edit_phone('1234567890', '1112223333')

    print(john)

    found_phone = john.find_phone('5555555555')
    print(f"{john.name}: {found_phone}")

    book.delete('Jane')


if __name__ == '__main__':
    main()
