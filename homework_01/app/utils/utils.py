def display_menu(menu_dict: dict) -> None:
    """
    Выводим на экран меню программы
    """
    max_len = max([len(value) for value in menu_dict.values()])
    menu_stars = '*' * (max_len + 12)

    print(f'\n\t\t\t{menu_stars}')
    for key, value in menu_dict.items():
        end_tab = max_len - len(value)
        print(f'\t\t\t*\t{key}. {value}{" " * end_tab}\t*')
    print(f'\t\t\t{menu_stars}\n')


def get_show_menu_item(menu_dict: dict) -> int:
    """
    Возвращает минимальный пункт меню,
    в котором повторно выводим на экран меню программы.
    Используется как первый выбранный пункт
    """
    return min([int(key) for key in menu_dict.keys()])


def get_max_dict_key(dict_int_key: dict) -> int:
    """
    Возвращает максимальный ключ в словаре
    """
    return max([int(key) for key in dict_int_key.keys()])


def check_menu_item(menu_item: int, menu_dict: dict) -> bool:
    """
    Проверка введенного значения при выборе пункта меню
    """
    if menu_item in menu_dict:
        return True
    return False


def get_digit(user_message: str, error_message: str) -> int:
    """
    Проверка введенного значения на целое число,
    реализована совместно с вечным запросом правильного значения
    """
    item = input(user_message)
    while not item.isdigit():
        item = input(error_message)
    return int(item)


def get_yes_no(user_message: str, error_message: str) -> bool:
    """
    Проверка введенного значения на вопрос требующего ответа: да/нет
    """
    correct_answer = [['да', 'yes', 'y'], ['нет', 'no', 'not', 'n']]
    item = input(user_message).lower()
    while not (item in correct_answer[0] or item in correct_answer[1]):
        item = input(error_message).lower()
    if item in correct_answer[0]:
        return True
    if item in correct_answer[1]:
        return False
