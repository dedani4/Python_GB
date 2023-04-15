import text_fields as txt


def main_menu() -> int:
    print('''Main menu
    1. Open file
    2. Save file
    3. Show all contacts
    4. Create contact
    5. Search contact
    6. Change contact
    7. Delete contact
    8. Exit''')
    choice = ''
    while True:
        choice = input('Choose menu point: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Enter number from 1 to 8')


def show_contacts(book: list[dict], message: str):
    if book:
        print('\n' + '-' * 63)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print(63 * '-' + '\n')
    else:
        print(message)


def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def new_contact() -> dict:
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return {'name': name, 'phone': phone, 'comment': comment}


def confirm(message) -> bool:
    answer = input(message)
    if answer.lower() == 'y':
        return True
    else:
        return False


def search_request(message) -> str:
    return input(message)






