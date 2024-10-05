class Contact:
    def __init__(self, name, phone, mail, status, city, phone_book):
        self.__id = Contact._next_id(phone_book)
        self.__name = name
        self.__phone = phone
        self.__mail = mail
        self.__status = status
        self.__city = city

    @staticmethod
    def _next_id(phone_book):
        if phone_book:
            return max([int(key) for key in phone_book.keys()]) + 1
        return 1

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_mail(self, mail):
        self.__mail = mail

    def set_status(self, status):
        self.__status = status

    def set_city(self, city):
        self.__city = city

    def get_id(self):
        return self.__id

    def get_name(self):
        try:
            return self.__name
        except AttributeError:
            return None

    def get_phone(self):
        try:
            return self.__phone
        except AttributeError:
            return None

    def get_mail(self):
        try:
            return self.__mail
        except AttributeError:
            return None

    def get_status(self):
        try:
            return self.__status
        except AttributeError:
            return None

    def get_city(self):
        try:
            return self.__city
        except AttributeError:
            return None

    def get_contact(self):
        return {'name': self.get_name(),
                'phone': self.get_phone(),
                'mail': self.get_mail(),
                'status': self.get_status(),
                'city': self.get_city()}
