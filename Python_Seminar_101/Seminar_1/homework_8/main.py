import actions

if __name__ == '__main__':
    menu = {'1': 'show phonebook',
            '2': 'add new contact',
            '3': 'edit contact',
            '4': 'search contact',
            '5': 'delete contact',
            '6': 'main menu'}

    choice = '6'
    while choice == '6':
        print("\033[H\033[J")
        print('Main menu')
        for key in menu:
            print(key + ' ' + menu[key])
        choice = input('Select item: ')
        if choice == '1':
            actions.show_all()
            choice = input('Input 0 to quit or 6 to main menu:')

        if choice == '2':
            contact = input('input contact (name;phone;comment): ')
            actions.add_contact(contact)
            choice = input('Input 0 to quit or 6 to main menu:')

        if choice == '3':
            contact = input('input name to change contact: ')
            actions.edit_contact(contact)
            choice = input('Input 0 to quit or 6 to main menu:')

        if choice == '4':
            contact = input('input name of contact to search: ')
            actions.search_contact(contact)
            choice = input('Input 0 to quit or 6 to main menu:')

        if choice == '5':
            contact = input('input name of contact to delete: ')
            actions.delete_contact(contact)
            choice = input('Input 0 to quit or 6 to main menu:')
