import os.path
from os import path
from json import dump, load, JSONDecodeError

CONTACT_BASE = path.join('contact.db')

def get_max_dict_key(contact_base: dict) -> int:
    """
    Возвращает максимальный ключ в словаре
    """
    try:
        max_id = max([int(key) for key in contact_base.keys()])
        return max_id
    except ValueError:
        return 1

def open_contact_base() -> dict:
    """
    Открываем файл с контактами
    Если файла нет, возвращаем пустой словарь
    """
    res = {}
    if os.path.exists(CONTACT_BASE):
        try:
            with open(CONTACT_BASE, 'r', encoding='utf-8') as file_r:
                res = load(file_r)
                return res
        except JSONDecodeError:
            return {'file': 'JSONDecodeError'}
    else:
        return {'file': 'no_file'}


def dump_contact_base(contact_base: dict) -> None:
    """
    Сохранение (полная перезапись файла) справочника контактов в файл на диск
    """
    with open(CONTACT_BASE, 'w', encoding='utf-8') as file_w:
        dump(contact_base, file_w, indent=4, ensure_ascii=False)


def add_contact(new_contact: dict[str: str]) -> None:
    """
    Добавление нового контакта, с ключем max(key) + 1
    """
    contact_base = open_contact_base()
    new_key = get_max_dict_key(contact_base) + 1
    contact_base[new_key] = new_contact
    dump_contact_base(contact_base)


def edit_contact(id_contact: int, new_contact: dict[str: str]) -> None:
    """
    Добавление нового контакта, с ключем max(key) + 1
    """
    contact_base = open_contact_base()
    contact_base[id_contact] = new_contact
    dump_contact_base(contact_base)