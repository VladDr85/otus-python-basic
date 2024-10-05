from json import dump, load, JSONDecodeError

import settings
import homework_01.app.utils.utils as ut


def main():
    phone_book_data = {}
    menu_item = ut.get_show_menu_item(settings.MENU_DICT)

    while True:
        match menu_item:
            case 1:
                ut.display_menu(settings.MENU_DICT)
            case 2:
                phone_book_data = open_phone_data(settings.PHONE_BASE)
            case 3:
                display_all_contact(phone_book_data)
            case 4:
                display_find_contact(phone_book_data)
            case 5:
                add_contact(phone_book_data)
            case 6:
                edit_contact(phone_book_data)
            case 7:
                del_contact(phone_book_data)
            case 8:
                dump_phone_book_data(phone_book_data)
            case 9:
                recover_phone_data(settings.PHONE_BOOK_BACKUP)
            case 10:
                dump_phone_book_data(phone_book_data)
                break

        while True:
            menu_item = ut.get_digit('\nВыберите пункт меню: ', 'Введите целое число: ')
            if ut.check_menu_item(menu_item, settings.MENU_DICT):
                break


def check_empty_phone_book(phone_book_data: dict) -> bool:
    """
    Проверка телефонного справочника на пустоту.
    Если справочник пустой, предложить его заполнить
    """
    if phone_book_data:
        return True
    else:
        print(f'\tТелефонный справочник пуст!'
              f'\tПопробуйте его открыть повторно, восстановить данные или заполнить самостоятельно')
        return False


def dump_phone_book_data(phone_book_data: dict) -> None:
    """
    Сохранение (полная перезапись файла) справочника контактов в файл на диск
    """
    if ut.get_yes_no('\n\tСохранить данные на диск? Укажите: y/n: ',
                     '\tОтвет не понятен. Укажите: y/n: '):
        with open(settings.PHONE_BASE, 'w', encoding='utf-8') as file_w:
            dump(phone_book_data, file_w, indent=4, ensure_ascii=False)
            print('\tДанные успешно сохранены!')


def input_data_save_contact(phone_book_data: dict, key_dict: int) -> None:
    """
    Ввод данный для нового контакта
    Добавлет или перезаписывает контакт, с дополнительным подтверждением
    """
    new_contact = {}
    new_key = key_dict

    print('\n\t\tУкажите новые данные:')
    new_contact['name'] = input('\tИмя:\t\t')
    new_contact['phone'] = input('\tТелефон:\t')
    new_contact['status'] = input('\tСтатус:\t\t')
    new_contact['city'] = input('\tГород:\t\t')

    print('\n\tПроверьте введенные данные перед сохранением!')
    print(f'\n\t\t\tКонтакт {new_key}')
    for key, value in new_contact.items():
        print(f'\t{key:<10}:\t{value:<15}')
    if ut.get_yes_no('\n\tСохранить данные? Укажите: y/n: ',
                     '\tОтвет не понятен. Укажите: y/n: '):
        phone_book_data[new_key] = new_contact
        print('\tДанные успешно сохранены!')


def del_contact(phone_book_data: dict) -> None:
    """
    Удаление контакта/тов по ключу поиска. Удаление проводится по одному контакту.
    Предлагается удалить каждый найденый контакт, с возможностью отказаться
    """
    search_list = find_contact(phone_book_data)
    print(f'\n\tУдаление всех найденных контаков, с возможностью пропустить при необходимости:')
    for search_id in search_list:
        search_dict = phone_book_data.get(search_id, 'Запись не найдена')
        print(f'\n\t\t\tКонтакт {search_id}')
        for key, value in search_dict.items():
            print(f'\t{key:<10}:\t{value:<15}')

        if ut.get_yes_no('\n\tПодтвердите удаление контакта? Укажите: y/n: ',
                         '\tОтвет не понятен. Укажите: y/n: '):
            del phone_book_data[search_id]


def edit_contact(phone_book_data: dict) -> None:
    """
    Изменение контакта/тов по ключу поиска
    Предлагается изменить каждый найденый контакт, с возможностью отказаться
    """
    search_list = find_contact(phone_book_data)
    print(f'\n\tИзменение всех найденных контаков, с возможностью пропустить при необходимости:')
    for search_id in search_list:
        search_dict = phone_book_data.get(search_id, 'Запись не найдена')
        print(f'\n\t\t\tКонтакт {search_id}')
        for key, value in search_dict.items():
            print(f'\t{key:<10}:\t{value:<15}')

        if ut.get_yes_no('\n\tПровести изменение контакта? Укажите: y/n: ',
                         '\tОтвет не понятен. Укажите: y/n: '):
            input_data_save_contact(phone_book_data, search_id)


def add_contact(phone_book_data: dict) -> None:
    """
    Добавление нового контакта, с ключем max(key) + 1
    Если спраочник пуст, уточнить желание начинать заполнение
    """
    if not check_empty_phone_book(phone_book_data):
        if ut.get_yes_no('\tЗаполнять пустой справочник? Укажите: y/n: ',
                         '\tОтвет не понятен. Укажите: y/n: '):
            pass
        else:
            return None

    new_key = ut.get_max_dict_key(phone_book_data) + 1
    input_data_save_contact(phone_book_data, new_key)


def find_contact(phone_book_data: dict) -> set:
    """
    Поиск по справочнику на основе полученной от пользователя информации.
    Возвращаем список с ключами найденных элементов
    """
    search_list = set()
    if check_empty_phone_book(phone_book_data):
        search_value = input('\tВведите значение для поиска по справочнику: ').lower()
        for contacts_id, contacts in phone_book_data.items():
            for key, value in contacts.items():
                if search_value in value.lower():
                    search_list.add(contacts_id)
        print(f'\tНайдено {len(search_list)} шт.')
    return search_list


def display_find_contact(phone_book_data: dict) -> None:
    """
    Вывод на экран найденых элементов по списку ключей
    """
    search_list = find_contact(phone_book_data)
    for search_id in search_list:
        search_dict = phone_book_data.get(search_id, 'Запись не найдена')
        print(f'\n\t\t\tКонтакт {search_id}')
        for key, value in search_dict.items():
            print(f'\t{key:<10}:\t{value:<15}')


def display_all_contact(phone_book_data: dict) -> None:
    """
    Выводим на экран весь телефонный справочник
    """
    if check_empty_phone_book(phone_book_data):
        for contacts_id, contacts in phone_book_data.items():
            print(f'\n\t\t\tКонтакт {contacts_id}')
            for key, value in contacts.items():
                print(f'\t{key:<10}:\t{value:<15}')


def recover_phone_data(phone_book_backup: dict) -> None:
    """
    Восстановить заводские данные в телефонном справочнике
    Используется если заигрались с изменениями и удалением
    """
    ut.get_yes_no('\tВосстановить заводские данные? Укажите: y/n: ',
                  '\tОтвет не понятен. Восстановить заводские данные? Укажите: y/n: ')
    with open(settings.PHONE_BASE, 'w', encoding='utf-8') as file_w:
        dump(phone_book_backup, file_w, ensure_ascii=False, indent=4)
        print('\tДанные восстановлены, теперь можно открыть телефонный справочник.')


def open_phone_data(phone_book: str) -> dict:
    """
    Открываем json файл с данными телефонного стправочника.
    Если файла нет, предлагаем востановить его из данных по умолчанию
    """
    try:
        with open(phone_book, 'r', encoding='utf-8') as file_r:
            phone_book_data = load(file_r)
            print(f'\tТелефонный справочник успешно открыт!')
            return phone_book_data
    except FileNotFoundError:
        print(f'\tТелефонный справочник {phone_book} не найден!')
        recover_phone_data(settings.PHONE_BOOK_BACKUP)
    except JSONDecodeError:
        print(f'\tТелефонный справочник {phone_book} открыт, но он пустой!')
        return {}


if __name__ == '__main__':
    main()
