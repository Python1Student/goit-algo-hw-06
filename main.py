from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    def __init__(self, name):
        if not name:
            raise ValueError
        Field.__init__(self, name)


class Phone(Field):
    # реалізація класу
    def __init__(self, number):
        if len(number) != 10 or not number.isdigit():
            raise ValueError
        Field.__init__(self, number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        result = Record.__find_phone(self, phone)
        return result

    def edit_phone(self, old_phone, new_phone):
        result = Record.__find_phone(self, old_phone)
        self.phones[self.phones.index(result)] = Phone(new_phone)

    def remove_phone(self, phone):
        result = Record.__find_phone(self, phone)
        self.phones.remove(result)

    def __find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name in book.data:
        print(book.data[name])

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


if __name__ == '__main__':
    main()
