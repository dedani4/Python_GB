main_menu = '''Main menu
    1. Open file
    2. Save file
    3. Show all contacts
    4. Create contact
    5. Search contact
    6. Change contact
    7. Delete contact
    8. Exit'''

menu_choice = 'Choose menu point: '

no_contact_or_file = 'Phonebook is empty or closed'

load_successful = 'Phonebook was successfully loaded'
save_successful = 'Phonebook was successfully saved'

new_name = 'Input name of contact: '
new_phone = 'Input phone number of contact: '
new_comment = 'Input comment for contact: '


def new_contact_successful(name):
    return f'New contact {name} was successfully added'


def change_successful(name):
    return f'Contact {name} was successfully changed'


is_changed = 'Phonebook was changed. Save it? (y/n): '
bye_bye = 'Thank you for using phonebook!'

search_name = 'Input name to search for: '
change_contact = 'Input number of contact to change: '
update_contact = 'Input new data of contact or skip'
delete_contact_index = 'Input index to delete contact: '

contact_with_change = 'Input contact with changes: '

no_contact_found = 'No such a contact'


def delete_question(name):
    return f'Delete contact {name}? (y/n): '


def delete_successful(name):
    return f'Contact {name} was successfully deleted'


change_question = 'Change this contact? (y/n): '
