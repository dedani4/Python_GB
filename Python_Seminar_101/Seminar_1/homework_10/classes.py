class Contact:
    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def cnt_to_str(self):
        return f'{self.name}:{self.phone}:{self.comment}'

    def __str__(self):
        return f'{self.name:<20}{self.phone:<20}{self.comment:<20}'

    def edit(self, name: str, phone: str, comment: str = ''):
        self.name = name if name else self.name
        self.phone = phone if phone else self.phone
        self.comment = comment if comment else self.comment


class Phonebook:
    def __init__(self, path: str):
        self.path = path
        self.phonebook: list[Contact] = []
        self.is_changed = False

    def open_file(self):
        self.phonebook.clear()
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for contact in data:
            contact_list = contact.strip().split(':')
            self.phonebook.append(Contact(contact_list[0], contact_list[1], contact_list[2]))

    def save_file(self):
        save_book = []
        for contact in self.phonebook:
            save_book.append(contact.cnt_to_str())
        data = '\n'.join(save_book)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)
        self.is_changed = False

    def get(self):
        return self.phonebook

    def add(self, contact: Contact) -> None:
        self.phonebook.append(contact)
        self.is_changed = True

    def search_contact(self, request: str) -> list[Contact]:
        result = []
        for contact in self.phonebook:
            if request in contact.cnt_to_str().lower():
                result.append(contact)
        return result

    def edit_contact(self, edited_contact: list[int, Contact]) -> None:
        index, new = edited_contact
        self.phonebook[index].edit(new.name, new.phone, new.comment)
        self.is_changed = True

    def remove(self, index: int) -> str:
        deleted_element = self.phonebook.pop(index)
        self.is_changed = True
        return deleted_element.name

    def self_on_exit(self):
        return self.is_changed
