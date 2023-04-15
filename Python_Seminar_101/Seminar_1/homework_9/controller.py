import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                request = view.search_request(txt.search_name)
                contact = model.search_contact(request)
                view.show_contacts(contact, txt.no_contact_found)
            case 6:
                request = view.search_request(txt.change_name)
                contact = model.search_contact(request)
                view.show_contacts(contact, txt.no_contact_found)
                if contact:
                    if view.confirm(txt.change_question):
                        contact = view.new_contact()
                        model.add_contact(contact)
                        model.delete_contact(request)
                        view.print_info(txt.change_successful)
            case 7:
                request = view.search_request(txt.delete_name)
                contact = model.search_contact(request)
                view.show_contacts(contact, txt.no_contact_found)
                if contact:
                    if view.confirm(txt.delete_question):
                        model.delete_contact(request)
                        view.print_info(txt.delete_successful)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                    view.print_info(txt.bye_bye)
                    exit()
