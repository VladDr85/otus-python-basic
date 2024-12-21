import pytest
from homework_02.app.model.contacts import Contact

@pytest.fixture
def contact():
    return Contact('John Doe', '1234567890', 'john@example.com', 'Friend', 'New York', {})

def test_contact_initialization(contact):
    assert contact.get_name() == 'John Doe'
    assert contact.get_phone() == '1234567890'
    assert contact.get_mail() == 'john@example.com'
    assert contact.get_status() == 'Friend'
    assert contact.get_city() == 'New York'
    assert contact.get_id() == 1  # Проверяем, что ID установлен правильно

def test_set_name(contact):
    contact.set_name('Jane Doe')
    assert contact.get_name() == 'Jane Doe'

def test_set_phone(contact):
    contact.set_phone('0987654321')
    assert contact.get_phone() == '0987654321'

def test_set_mail(contact):
    contact.set_mail('jane@example.com')
    assert contact.get_mail() == 'jane@example.com'

def test_set_status(contact):
    contact.set_status('Colleague')
    assert contact.get_status() == 'Colleague'

def test_set_city(contact):
    contact.set_city('Los Angeles')
    assert contact.get_city() == 'Los Angeles'

def test_get_contact(contact):
    expected_contact_info = {
        'name': 'John Doe',
        'phone': '1234567890',
        'mail': 'john@example.com',
        'status': 'Friend',
        'city': 'New York'
    }
    assert contact.get_contact() == expected_contact_info

def test_next_id_with_empty_phone_book():
    phone_book = {}
    new_id = Contact._next_id(phone_book)
    assert new_id == 1  # Если телефонная книга пуста, ID должен быть 1

def test_next_id_with_existing_phone_book():
    phone_book = {1: 'Contact 1', 2: 'Contact 2'}
    new_id = Contact._next_id(phone_book)
    assert new_id == 3  # Новый ID должен быть максимальным + 1
