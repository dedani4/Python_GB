phonebook = []
start_phonebook = []
PATH = 'phonebook.txt'


def get_pb():
    global phonebook
    return phonebook


def load_file():
    global phonebook
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phonebook.append({'name': contact[0],
                          'phone': contact[1],
                          'comment': contact[2]})
    start_phonebook = phonebook.copy()


def save_file():
    global phonebook
    data = []
    for contact in phonebook:
        data.append(':'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    global phonebook
    phonebook.append(contact)


def exit_pb() -> bool:
    global phonebook, start_phonebook
    if phonebook == start_phonebook:
        return False
    else:
        return True


def search_contact(request):
    global phonebook
    for contact in phonebook:
        if request in contact['name'].lower():
            return [contact]


def delete_contact(request):
    global phonebook
    for contact in phonebook:
        if request in contact['name']:
            phonebook.remove(contact)
