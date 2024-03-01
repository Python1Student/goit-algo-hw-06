from constants import *
from functions import parse_input, add_contact, read_contact


def main():
    print(BOT + 'Welcome to assistant Bot!')

    while True:
        user_input = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
        command, *args = parse_input(user_input) if len(user_input.split()) >= 1 else (None, 'None', 'None')

        # Для закриття
        if command in ('exit', 'close'):
            print(BOT + 'Good Bye!')
            break

        # Вітаємося
        elif command == 'hello':
            print(BOT + 'How can I help you?')

        # Додаємо або змінюємо контакт
        elif command in ('add', 'change'):
            # Перевіряємо чи 2 аргумента
            print(add_contact(*args))

        # Для виводу одного контаку
        elif command == 'phone':
            # Перевіряємо чи є аргументи
            print(read_contact(*args))

        # Для виводу всіх контактів
        elif command == 'all':
            print(read_contact(False))

        # Якщо користувач не ввів жодну з можливих команд ми даємо знати йому про це
        else: print(ERROR + 'Invalid Command')

# Перевіряємо чи це точка входу
if __name__ == '__main__':
    main()