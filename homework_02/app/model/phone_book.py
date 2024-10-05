import os.path
from pickle import dump, load
import homework_02.app.utils.utils_app as ut
import homework_02.app.view.view_app as vw
import homework_02.app.model.settings as settings
from homework_02.app.model.contacts import Contact


class PhoneBook:
    def __init__(self, phone_book_db):
        self.phone_book_db = phone_book_db
        self._phone_book_data = {}

    @staticmethod
    def check_empty_phone_book(phone_book_data):
        """
        Проверка телефонного справочника на пустоту.
        Если справочник пустой, предложить его заполнить
        """
        if phone_book_data:
            return True
        else:
            vw.message_empty_phone_book()
            return False

    @staticmethod
    def find_contact(phone_book_data: dict) -> set:
        """
        Поиск по справочнику на основе полученной от пользователя информации.
        Возвращаем список с ключами найденных элементов
        """
        search_list = set()
        search_value = ut.input_lower('\tВведите значение для поиска: ')
        for contacts_id, contacts in phone_book_data.items():
            for value in contacts.get_contact().values():
                if search_value in str(value).lower():
                    search_list.add(contacts_id)
        vw.message_search_contact_count(len(search_list))
        return search_list

    @staticmethod
    def get_contact_attributes():
        name = ut.input_capitalize('\tИмя:\t\t')
        phone = ut.input_capitalize('\tТелефон:\t')
        mail = ut.input_capitalize('\tMail:\t\t')
        status = ut.input_capitalize('\tСтатус:\t\t')
        city = ut.input_capitalize('\tГород:\t\t')
        return name, phone, mail, status, city

    def get_phone_book_data(self):
        return self._phone_book_data

    def dump_phone_book(self):
        """
        Сохранение (полная перезапись файла) справочника контактов в файл на диск
        """
        with open(self.phone_book_db, "wb") as file_wb:
            dump(self._phone_book_data, file_wb)

    def recover_phone_data(self):
        """
        Восстановить заводские данные в телефонном справочнике
        Используется если заигрались с изменениями и удалением
        """
        if ut.get_yes_no('\tВосстановить заводские данные? Укажите: y/n: ',
                         '\tОтвет не понятен. Восстановить заводские данные? Укажите: y/n: '):
            self._phone_book_data = {}
            for value in settings.PHONE_BOOK_BACKUP.values():
                new_contact = Contact(value['name'],
                                      value['phone'],
                                      value['mail'],
                                      value['status'],
                                      value['city'],
                                      self._phone_book_data)
                new_contact_id = new_contact.get_id()
                self._phone_book_data[new_contact_id] = new_contact
            PhoneBook.dump_phone_book(self)
            vw.message_successful_recover(self.phone_book_db)

    def open_phone_data(self):
        """
        Открываем файл с данными телефонного стправочника.
        Если файла нет, предлагаем востановить его из данных по умолчанию
        """
        if os.path.exists(self.phone_book_db):
            with open(self.phone_book_db, 'rb') as file_rb:
                load_val = load(file_rb)
                for contacts_id in load_val:
                    self._phone_book_data[contacts_id] = load_val[contacts_id]
            if self._phone_book_data:
                vw.message_successful_load(self.phone_book_db)
            else:
                vw.message_empty_phone_book()
        else:
            vw.message_file_not_found(self.phone_book_db)
            self._phone_book_data = {}

    def display_all_contact(self):
        """
        Выводим на экран весь телефонный справочник.
        Если он пустой то не выводим
        """
        if PhoneBook.check_empty_phone_book(self._phone_book_data):
            for contacts_id in self._phone_book_data:
                contact = self._phone_book_data[contacts_id]
                vw.display_contact_info(contact.get_contact())

    def add_new_contact(self):
        """
        Добавление нового контакта, с ключем max(key) + 1
        Если спраочник пуст, уточнить желание начинать заполнение
        """
        vw.message_add_new_contact()
        name, phone, mail, status, city = PhoneBook.get_contact_attributes()
        new_contact = Contact(name, phone, mail, status, city, self._phone_book_data)
        new_contact_id = new_contact.get_id()

        vw.check_new_contact(new_contact.get_contact())
        if ut.get_yes_no('\n\tСохранить данные? Укажите: y/n: ',
                         '\tОтвет не понятен. Укажите: y/n: '):
            self._phone_book_data[new_contact_id] = new_contact
            vw.message_successfully_saved()

    def add_contact(self):
        """
        Добавление нового контакта, с ключем max(key) + 1
        Если спраочник пуст, уточнить желание начинать заполнение
        """
        if PhoneBook.check_empty_phone_book(self._phone_book_data):
            PhoneBook.add_new_contact(self)
        else:
            if ut.get_yes_no('\tЗаполнять пустой справочник? Укажите: y/n: ',
                             '\tОтвет не понятен. Укажите: y/n: '):
                PhoneBook.add_new_contact(self)

    def display_find_contact(self):
        """
        Вывод на экран найденых контактов по списку ключей
        Несли ничего не найдено, то не выводим информацию
        """
        search_list = PhoneBook.find_contact(self._phone_book_data)
        if search_list:
            for search_id in search_list:
                contact = self._phone_book_data[search_id]
                vw.display_contact_info(contact.get_contact())

    def del_contact(self):
        """
        Удаление контакта/тов по ключу поиска. Удаление проводится по одному контакту.
        Предлагается удалить каждый найденый контакт, с возможностью отказаться
        """
        search_list = PhoneBook.find_contact(self._phone_book_data)
        if search_list:
            vw.message_delete_info()

            for search_id in search_list:
                contact = self._phone_book_data.get(search_id, 'Запись не найдена')
                vw.display_contact_info(contact.get_contact())
                if ut.get_yes_no('\n\tПодтвердите удаление контакта? Укажите: y/n: ',
                                 '\tОтвет не понятен. Укажите: y/n: '):
                    del self._phone_book_data[search_id]
                    vw.message_successfully_delete()

    def edit_contact(self):
        """
        Изменение контакта/тов по ключу поиска
        Предлагается изменить каждый найденый контакт, с возможностью отказаться
        """
        search_list = PhoneBook.find_contact(self._phone_book_data)
        if search_list:
            if ut.get_yes_no('\n\tИзменить весь контак (y) или конкретные атрибуты (n): y/n: ',
                             '\tОтвет не понятен. Укажите: y/n: '):
                for search_id in search_list:
                    contact = self._phone_book_data.get(search_id, 'Запись не найдена')
                    vw.display_contact_info(contact.get_contact())

                    if ut.get_yes_no(f'\n\tПровести изменение контакта: {contact.get_name()}? Укажите: y/n: ',
                                     f'\tОтвет не понятен. Укажите: y/n: '):
                        PhoneBook.add_new_contact(self)
                        del self._phone_book_data[search_id]
            else:
                vw.message_edit_attributes()
                name, phone, mail, status, city = PhoneBook.get_contact_attributes()
                for search_id in search_list:
                    contact = self._phone_book_data.get(search_id, 'Запись не найдена')
                    if name:
                        contact.set_name(name)
                    if phone:
                        contact.set_phone(phone)
                    if mail:
                        contact.set_mail(mail)
                    if status:
                        contact.set_status(status)
                    if city:
                        contact.set_city(city)
                vw.message_successfully_saved()
