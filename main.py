from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError
        Field.__init__(self, name)


class Phone(Field):
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
        return self.__find_phone(phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(self.__find_phone(old_phone))] = Phone(new_phone)

    def remove_phone(self, phone):
        self.phones.remove(self.__find_phone(phone))

    def __find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError
        self.data[record.name.value] = record

    def find(self, name):
        return self.__find(name)

    def delete(self, name):
    	if self.__find(name):
        	del self.data[name] 

    def __find(self, name):
        result = self.data.get(name, None)
        if result is None:
            raise KeyError
        return result


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name in book.data:
        print(book.data[name])
        
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")


if __name__ == '__main__':
    main()
