import pytest
from unittest.mock import patch, MagicMock
from homework_02.app.model.phone_book import PhoneBook
from homework_02.app.model.contacts import Contact


@pytest.fixture
def phone_book():
    pb = PhoneBook("test_phone_book.dmp")
    # Добавим несколько контактов для тестирования
    contact1 = Contact("Иван", "+79183875754", "ivan_mail@mail.ru", "Друг", "Краснодар", pb.get_phone_book_data())
    pb.get_phone_book_data()[contact1.get_id()] = contact1
    contact2 = Contact("Татьяна", "+79183299751", "tanya_mail@mail.ru", "Семья", "Краснодар", pb.get_phone_book_data())
    pb.get_phone_book_data()[contact2.get_id()] = contact2
    print(pb.get_phone_book_data())
    pb.display_all_contact()
    return pb


def test_edit_contact_full(phone_book):
    # Имитация ввода пользователя
    with patch('homework_02.app.utils.utils_app.get_yes_no', side_effect=[True, True]), \
            patch('homework_02.app.utils.utils_app.input_capitalize',
                  side_effect=["Павел", "+79183225944", "pavel_mail@mail.ru", "Друг", "Москва"]), \
            patch('homework_02.app.utils.utils_app.input_lower', return_value="Иван"), \
            patch.object(phone_book, 'find_contact', return_value={"Иван"}):  # Имитация поиска контакта по ID 1

        # Убедимся, что контакт с ID 1 - это "Иван"
        assert phone_book.get_phone_book_data()[1].get_name() == "Иван"

        # Вызов метода редактирования
        phone_book.edit_contact()

        # Проверяем, что контакт с ID 1 был изменен
        assert phone_book.get_phone_book_data()[1].get_name() == "Павел"
        assert phone_book.get_phone_book_data()[1].get_phone() == "+79183225944"
        assert phone_book.get_phone_book_data()[1].get_mail() == "pavel_mail@mail.ru"
        assert phone_book.get_phone_book_data()[1].get_status() == "Друг"
        assert phone_book.get_phone_book_data()[1].get_city() == "Москва"


def test_edit_contact_partial(phone_book):
    # Имитация ввода пользователя
    with patch('homework_02.app.utils.utils_app.get_yes_no', side_effect=[False, True]), \
            patch('homework_02.app.utils.utils_app.input_capitalize', side_effect=["", "+79183225944", "", "", ""]), \
            patch('homework_02.app.utils.utils_app.input_lower', return_value="Татьяна"), \
            patch.object(phone_book, 'find_contact', return_value={2}):  # Имитация поиска контакта по ID 2

        phone_book.edit_contact()

        # Проверяем, что только телефон был изменен
        assert phone_book.get_phone_book_data()[2].get_name() == "Татьяна"
        assert phone_book.get_phone_book_data()[2].get_phone() == "+79183225944"
        assert phone_book.get_phone_book_data()[2].get_mail() == "tanya_mail@mail.ru"
        assert phone_book.get_phone_book_data()[2].get_status() == "Семья"
        assert phone_book.get_phone_book_data()[2].get_city() == "Краснодар"


def test_edit_contact_no_contacts(phone_book):
    # Удаляем все контакты
    phone_book.get_phone_book_data().clear()

    with patch('homework_02.app.utils.utils_app.get_yes_no', return_value=True), \
            patch('homework_02.app.utils.utils_app.input_lower', return_value="Неважно"), \
            patch.object(phone_book, 'find_contact', return_value=set()):  # Имитация отсутствия контактов

        phone_book.edit_contact()

        # Проверяем, что ничего не изменилось
        assert len(phone_book.get_phone_book_data()) == 0
