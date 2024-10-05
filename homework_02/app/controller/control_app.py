import homework_02.app.utils.utils_app as ut
import homework_02.app.view.view_app as vw
import homework_02.app.model.settings as settings
from homework_02.app.model.phone_book import PhoneBook


def start_app():
    phone_book_data = PhoneBook(settings.PHONE_BASE_DMP)
    menu_item = ut.get_show_menu_item(settings.MENU_DICT)
    exit_item = ut.get_max_dict_key(settings.MENU_DICT)

    while menu_item != exit_item:
        match menu_item:
            case 1:
                vw.display_menu(settings.MENU_DICT)
            case 2:
                phone_book_data.open_phone_data()
            case 3:
                phone_book_data.display_all_contact()
            case 4:
                phone_book_data.display_find_contact()
            case 5:
                phone_book_data.add_contact()
            case 6:
                phone_book_data.edit_contact()
            case 7:
                phone_book_data.del_contact()
            case 8:
                phone_book_data.dump_phone_book()
            case 9:
                phone_book_data.recover_phone_data()

        count_choice = 0
        menu_item = 0
        while count_choice <= 3 and not ut.check_menu_item(menu_item, settings.MENU_DICT):
            menu_item = ut.get_digit('\nВыберите пункт меню: ', 'Введите целое число: ')
            count_choice += 1
        if not ut.check_menu_item(menu_item, settings.MENU_DICT):
            menu_item = ut.get_show_menu_item(settings.MENU_DICT)

    phone_book_data.dump_phone_book()
