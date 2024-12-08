import pytest
from unittest.mock import MagicMock
from homework_02.app.model.phone_book import PhoneBook
from homework_02.app.model.contacts import Contact
import homework_02.app.model.settings as settings


@pytest.fixture
def phone_book():
    """Фикстура для создания экземпляра PhoneBook."""
    return PhoneBook('test_phone_book.dmp')


def test_add_new_contact(mocker, phone_book):
    """Тест для добавления нового контакта."""
    # Мокаем функции, которые запрашивают ввод у пользователя
    mocker.patch('homework_02.app.view.view_app.check_new_contact')
    mocker.patch('homework_02.app.utils.utils_app.get_yes_no', return_value=True)

    # Мокаем ввод данных для нового контакта
    mocker.patch('homework_02.app.utils.utils_app.input_capitalize', side_effect=[
        'Иван', '+79183875754', 'ivan_mail@mail.ru', 'Друг', 'Краснодар'
    ])

    # Добавляем новый контакт
    phone_book.add_new_contact()

    # Проверяем, что контакт добавлен
    assert len(phone_book.get_phone_book_data()) == 1
    contact = list(phone_book.get_phone_book_data().values())[0]
    assert contact.get_name() == 'Иван'
    assert contact.get_phone() == '+79183875754'
    assert contact.get_mail() == 'ivan_mail@mail.ru'
    assert contact.get_status() == 'Друг'
    assert contact.get_city() == 'Краснодар'


def test_display_all_contact(mocker, phone_book):
    """Тест для отображения всех контактов."""
    contact = Contact('Иван', '+79183875754', 'ivan_mail@mail.ru', 'Друг', 'Краснодар',
                      phone_book.get_phone_book_data())
    phone_book.get_phone_book_data()[contact.get_id()] = contact

    mock_display = mocker.patch('homework_02.app.view.view_app.display_contact_info')
    phone_book.display_all_contact()
    mock_display.assert_called_once_with(contact.get_contact())


def test_find_contact(mocker, phone_book):
    """Тест для поиска контакта."""
    contact = Contact('Иван', '+79183875754', 'ivan_mail@mail.ru', 'Друг', 'Краснодар', phone_book.get_phone_book_data())
    phone_book.get_phone_book_data()[contact.get_id()] = contact

    # Мокаем ввод для поиска
    mocker.patch('homework_02.app.utils.utils_app.input_lower', return_value='иван')

    # Вызываем метод find_contact
    found_contacts = phone_book.find_contact(phone_book.get_phone_book_data())

    # Проверяем, что контакт найден
    assert contact.get_id() in found_contacts

def test_del_contact(mocker, phone_book):
    """Тест для удаления контакта."""
    contact = Contact('Иван', '+79183875754', 'ivan_mail@mail.ru', 'Друг', 'Краснодар', phone_book.get_phone_book_data())
    phone_book.get_phone_book_data()[contact.get_id()] = contact

    # Мокаем метод find_contact, чтобы вернуть идентификатор контакта
    mocker.patch('homework_02.app.model.phone_book.PhoneBook.find_contact', return_value={contact.get_id()})

    # Мокаем подтверждение удаления
    mocker.patch('homework_02.app.utils.utils_app.get_yes_no', return_value=True)

    # Вызываем метод del_contact
    phone_book.del_contact()

    # Проверяем, что контакт удален
    assert contact.get_id() not in phone_book.get_phone_book_data()


def test_edit_contact(mocker, phone_book):
    """Тест для редактирования контакта."""
    # Создаем контакт и добавляем его в телефонный справочник
    contact = Contact('Иван', '+79183875754', 'ivan_mail@mail.ru', 'Друг', 'Краснодар', phone_book.get_phone_book_data())
    phone_book.get_phone_book_data()[contact.get_id()] = contact

    # Мокаем метод find_contact, чтобы вернуть идентификатор контакта
    mocker.patch('homework_02.app.model.phone_book.PhoneBook.find_contact', return_value={contact.get_id()})

    # Мокаем оба вызова get_yes_no, чтобы вернуть True
    mocker.patch('homework_02.app.utils.utils_app.get_yes_no', side_effect=[True, True])

    # Мокаем ввод новых данных для редактирования
    mocker.patch('homework_02.app.utils.utils_app.input_capitalize', side_effect=[
        'Петр', '+79180000000', 'petr@mail.ru', 'Друг', 'Москва'
    ])

    # Вызываем метод edit_contact
    phone_book.edit_contact()

    # Проверяем, что контакт обновлен
    updated_contact = phone_book.get_phone_book_data()[contact.get_id()]
    assert updated_contact.get_name() == 'Петр'
    assert updated_contact.get_phone() == '+79180000000'
    assert updated_contact.get_mail() == 'petr@mail.ru'
    assert updated_contact.get_status() == 'Друг'
    assert updated_contact.get_city() == 'Москва'


def test_recover_phone_data(mocker, phone_book):
    """Тест для восстановления данных телефона."""
    mocker.patch('homework_02.app.utils.utils_app.get_yes_no', return_value=True)
    phone_book.recover_phone_data()
    assert len(phone_book.get_phone_book_data()) == len(settings.PHONE_BOOK_BACKUP)


if __name__ == '__main__':
    pytest.main()
