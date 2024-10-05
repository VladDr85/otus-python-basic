import os
from pickle import dump
from homework_02.app.utils import utils_app as ut
from homework_02.app.model.phone_book import PhoneBook
import homework_02.app.model.settings as settings


class TestPhoneBook:
    @staticmethod
    def _remove_base():
        if os.path.exists(settings.TEST_PHONE_BASE_DMP):
            os.remove(settings.TEST_PHONE_BASE_DMP)

    @staticmethod
    def _create_base(phone_book_full):
        with open(settings.TEST_PHONE_BASE_DMP, "wb") as file_wb:
            dump(phone_book_full._phone_book_data, file_wb)

    def test_get_phone_book_data(self, phone_book_empty):
        assert phone_book_empty == {}

    def test_dump_phone_book(self):
        self._remove_base()
        test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
        test_phone_book.dump_phone_book()
        assert os.path.exists(settings.TEST_PHONE_BASE_DMP)

    def test_recover_phone_data(self):
        dict_phone_data = {}
        ut.input = lambda x: 'y'
        test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
        test_phone_book.recover_phone_data()
        for value in test_phone_book._phone_book_data.values():
            dict_phone_data[value.get_id()] = value.get_contact()
        assert dict_phone_data == settings.PHONE_BOOK_BACKUP

    def test_open_phone_data_no_file(self):
        self._remove_base()
        test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
        test_phone_book.open_phone_data()
        assert test_phone_book._phone_book_data == {}

    def test_open_phone_data_exists_file(self, phone_book_full):
        self._create_base(phone_book_full)
        dict_phone_data_open = {}
        dict_phone_data_fixture = {}

        with open(settings.TEST_PHONE_BASE_DMP, "wb") as file_wb:
            dump(phone_book_full._phone_book_data, file_wb)

        test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
        test_phone_book.open_phone_data()

        for value in test_phone_book._phone_book_data.values():
            dict_phone_data_open[value.get_id()] = value.get_contact()

        for value in phone_book_full._phone_book_data.values():
            dict_phone_data_fixture[value.get_id()] = value.get_contact()
        assert dict_phone_data_open == dict_phone_data_fixture
