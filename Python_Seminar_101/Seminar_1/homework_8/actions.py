def show_all():
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    print(''.join(data))
    file.close()


def add_contact(contact):
    file = open('phonebook.txt', 'a', encoding='UTF-8')
    file.write('\n' + contact)
    file.close()


def edit_contact(contact):
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for index, item in enumerate(data):
        if contact.lower() in item.lower():
            print(item)
            data[index] = input('input contact with update (name;phone;comment): ')
    file = open('phonebook.txt', 'w', encoding='UTF-8')
    for line in data:
        file.write(line)
        if '\n' not in line:
            file.write('\n')
    file.close()


def search_contact(contact):
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for line in data:
        line_split = line.split(';')
        if contact.lower() in line_split[0].lower():
            print(' '.join(line_split))
    file.close()


def delete_contact(contact):
    file = open('phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for index, item in enumerate(data):
        if contact.lower() in item.lower():
            print(item)
            data.remove(item)
    file = open('phonebook.txt', 'w', encoding='UTF-8')
    for line in data:
        file.write(line)
        if '\n' not in line:
            file.write('\n')
    file.close()
