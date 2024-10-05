import os
import pytest
import homework_02.app.model.settings as settings
from homework_02.app.model.contacts import Contact
from homework_02.app.model.phone_book import PhoneBook


@pytest.fixture(scope="session", autouse=True)
def get_test_contact():
    test_contact = {'name': 'Иван',
                    'phone': '+79183875754',
                    'mail': 'ivan_mail@mail.ru',
                    'status': 'Друг',
                    'city': 'Краснодар'}
    return test_contact


@pytest.fixture(scope="session", autouse=True)
def contact_full(get_test_contact):
    test_contact = get_test_contact
    test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
    test_contact_full = Contact(test_contact['name'],
                                test_contact['phone'],
                                test_contact['mail'],
                                test_contact['status'],
                                test_contact['city'],
                                test_phone_book.get_phone_book_data())
    return test_contact_full


@pytest.fixture(scope="session", autouse=True)
def contact_empty():
    test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
    test_contact_empty = Contact('', '', '', '', '', test_phone_book.get_phone_book_data())
    return test_contact_empty


@pytest.fixture(scope="session", autouse=True)
def phone_book_full(contact_full):
    phone_book_test = PhoneBook(settings.TEST_PHONE_BASE_DMP)
    phone_book_test._phone_book_data[contact_full.get_id()] = contact_full
    test_contact_empty = Contact('', '', '', '', '', phone_book_test.get_phone_book_data())
    phone_book_test._phone_book_data[test_contact_empty.get_id()] = test_contact_empty
    return phone_book_test


@pytest.fixture(scope="session", autouse=True)
def phone_book_empty():
    test_phone_book = PhoneBook(settings.TEST_PHONE_BASE_DMP)
    return test_phone_book._phone_book_data


@pytest.fixture(scope="session", autouse=True)
def remove_phone_book_base():
    if os.path.exists(settings.TEST_PHONE_BASE_DMP):
        os.remove(settings.TEST_PHONE_BASE_DMP)
    yield
    if os.path.exists(settings.TEST_PHONE_BASE_DMP):
        os.remove(settings.TEST_PHONE_BASE_DMP)
