import view
import text_fields as txt
from classes import Phonebook


def start_pb():
    phonebook_new = Phonebook('phonebook.txt')
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                phonebook_new.open_file()
                view.print_info(txt.load_successful)
            case 2:
                phonebook_new.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = phonebook_new.get()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                phonebook_new.add(contact)
                view.print_info(txt.new_contact_successful(contact.name))
            case 5:
                request = view.search_request(txt.search_name)
                contact = phonebook_new.search_contact(request)
                view.show_contacts(contact, txt.no_contact_found)
            case 6:
                pb = phonebook_new.get()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    edited_contact = view.choose_and_edit_contact(pb)
                    phonebook_new.edit_contact(edited_contact)
                    view.print_info(txt.change_successful(edited_contact[1].name))
            case 7:
                pb = phonebook_new.get()
                view.show_contacts(pb, txt.no_contact_or_file)
                if pb:
                    index = view.input_index(pb)
                    if view.confirm(txt.delete_question(pb[index].name)):
                        view.print_info(txt.delete_successful(phonebook_new.remove(index)))
            case 8:
                if phonebook_new.self_on_exit():
                    if view.confirm(txt.is_changed):
                        phonebook_new.save_file()
                view.print_info(txt.bye_bye)
                exit()
