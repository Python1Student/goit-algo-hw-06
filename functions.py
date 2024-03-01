from constants import *


# Функція для парсингу данних
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Читаємо файл з контактами
def read_file() -> dict:
    contacts = {}

    # Читаємо файл
    with open('contacts.txt', 'r') as file:
        # Робимо список зі строк
        lines = file.readlines()
    
    # Парсимо строку
    for line in lines:
        line = line.strip().split()

        # Додаємо строку до словника
        contacts[line[0]] = line[1]

    # Повертаємо словник
    return contacts


# Новий декоратор, який об'єднує всі інші декоратори
def handle_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return ERROR + "Give me name and phone please"
        except FileNotFoundError:
            return ERROR + "File Not Found"
        except TypeError:
            return ERROR + "Give me name and phone please"
    return inner


@handle_errors
# Функція для додавання та модифікації словника
def add_contact(name: str, number: str) -> str:
    # Читаємо файл та присвоюємо його значення в словник
    contacts = read_file()
    # Додаємо наш контакт до словника або замінюємо якщо є
    contacts[name] = number
    # Записуємо словник в файл
    with open('contacts.txt', 'w') as file:
        for key, value in contacts.items():    
            file.write(f'{key} {value}\n')

    # Повертаємо успішне виконання
    return BOT + 'Successful!'


@handle_errors
# Функція Для читання контактів
def read_contact(name: str) -> str:
    # Читаємо файл та присвоюємо його значення в словник
    contacts = read_file()

    # Перевіряємо чи шукаємо ми один контакт чи всі
    if not name:
        text = BOT + 'Contacts:\n'
        for key, value in contacts.items(): 
            text += f'{key} {value}'
            if key != list(contacts.keys())[-1]: text += '\n'
        return text
    
    # Повертаємо імя яке шукали
    return BOT + f'{name} {contacts[name]}'