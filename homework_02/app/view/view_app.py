def display_menu(menu_dict: dict) -> None:
    """
    Выводим на экран меню программы
    """
    max_len = max([len(value) for value in menu_dict.values()])
    menu_stars = '*' * (max_len + 12)

    print(f'\n\t\t\t{menu_stars}')
    for key, value in menu_dict.items():
        end_tab = max_len - len(value)
        print(f'\t\t\t*\t{key}.\t{value}{" " * end_tab}\t*')
    print(f'\t\t\t{menu_stars}\n')


def display_contact_info(contact_info: dict) -> None:
    """
    Выводим на экран карточку контакта
    """
    max_len_key = max([len(str(key)) for key in contact_info.keys()])
    max_len_value = max([len(str(value)) for value in contact_info.values()])
    top_bottom_line = '*' * (max_len_key + max_len_value + 10)

    print(f'\n\t\t\t\tКонтакт {contact_info['name']}')
    print(f'\t\t\t{top_bottom_line}')
    for key, value in contact_info.items():
        end_key = max_len_key - len(str(key))
        end_value = max_len_value - len(str(value))
        print(f'\t\t\t*   {key}{" " * end_key}: {value}{" " * end_value}   *')
    print(f'\t\t\t{top_bottom_line}')


def message_empty_phone_book() -> None:
    """
    Сообщение пользователю при пустом телефонном справочнике
    """
    print(f'\tТелефонный справочник пуст!'
          f'\tПопробуйте его открыть повторно, восстановить данные или заполнить самостоятельно')


def message_search_contact_count(contact_count) -> None:
    """
    Сообщение пользователю о количестве найденных контактов
    """
    print(f'\tНайдено контактов: {contact_count} шт.')


def message_successful_load(file_phone_book) -> None:
    """
    Сообщение пользователю об успешной загрузке телефонного справочника
    """
    print(f'\tТелефонный справочник {file_phone_book} успешно загружен')


def message_successful_recover(file_phone_book) -> None:
    """
    Сообщение пользователю о востановлении телефонного справочника из резервной копии
    """
    print(f'\tТелефонный справочник {file_phone_book} успешно восстановлен из резервной копии и открыт для работы')


def message_file_not_found(file_phone_book) -> None:
    """
    Сообщение пользователю о том, что файл с телефонным справочником не найден
    """
    print(f'\tФайл с данными {file_phone_book} отсуствует, будет создан новый файл с телефонным справочников')


def check_new_contact(contact_data) -> None:
    """
    Сообщение пользователю о проверке введенных данных перед сохранением
    """
    print('\n\tПроверьте введенные данные перед сохранением!')
    display_contact_info(contact_data)


def message_successfully_saved() -> None:
    """
    Сообщение пользователю об успешном сохранении данных
    """
    print('\tДанные успешно сохранены!')


def message_successfully_delete() -> None:
    """
    Сообщение пользователю об успешном удалении данных
    """
    print('\t\tЗапись удалена!')


def message_delete_info() -> None:
    """
    Сообщение пользователю о начале удаления и возможности пропустить элемент
    """
    print(f'\n\tУдаление всех найденных контаков, с возможностью пропустить при необходимости:')


def message_edit_attributes() -> None:
    """
    Сообщение пользователю о начале редактирования атрибутов контакта
    """
    print(f'\n\tУкажите новые данные для выбранных контактов:'
          f'\n\tЕсли атрибует не требуется менять, оставьте его пустым!\n')


def message_add_new_contact() -> None:
    """
    Сообщение пользователю перед созданием нового контакта
    """
    print('\n\tУкажите данные для нового контакта:')
