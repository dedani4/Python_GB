import text_fields as txt
from classes import Contact


def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice = input(txt.menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Enter number from 1 to 8')


def show_contacts(book: list[Contact], message: str):
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n}. {contact}')
        print(63 * '-' + '\n')
    else:
        print(message)


def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def new_contact() -> Contact:
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return Contact(name, phone, comment)


def confirm(message) -> bool:
    answer = input(message)
    if answer.lower() == 'y':
        return True
    else:
        return False


def search_request(message) -> str:
    return input(message)


def choose_and_edit_contact(book: list) -> list[int, Contact]:
    index = 0
    while 1 > index or index > len(book) + 1:
        choice = input(txt.change_contact)
        if choice.isdigit():
            index = int(choice)
    print(txt.update_contact)
    contact = new_contact()
    return [index - 1, contact]


def input_index(book: list) -> int:
    index = 0
    while 1 > index or index > len(book) + 1:
        choice = input(txt.delete_contact_index)
        if choice.isdigit():
            index = int(choice)
    return index - 1
