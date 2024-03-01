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
    def add_phone(self, phone):
          self.value.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.value.remove(phone)
        else:
            print('Phone not in List')

    def edit_phone(self, old, new):
        index = self.value.index(old)

        self.value.pop(index)

        self.value.insert(index, new)

    def find_phone(self, phone):
        if phone in self.value:
            return phone
        else:
            return 'PhoneNotFound'


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phone([])

    def add_phone(self, phone):
          self.phones.value.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.value.remove(phone)
        else:
            print('Phone not in List')

    def edit_phone(self, old, new):
        index = self.phones.value.index(old)

        self.phones.value.pop(index)

        self.phones.value.insert(index, new)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, obj: Record):
        print(self.data)
        self.data[str(obj.name)] = obj.phones

    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print('NameNotFound')
        
def main():       
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    book.delete("Jane")


main()