import pytest
from unittest.mock import patch
from homework_02.app.utils.utils_app import (
    get_show_menu_item,
    get_max_dict_key,
    check_menu_item,
    get_digit,
    get_yes_no,
    input_lower,
    input_capitalize
)

def test_get_show_menu_item():
    menu_dict = {1: 'Option 1', 2: 'Option 2', 3: 'Option 3'}
    result = get_show_menu_item(menu_dict)
    assert result == 1  # Минимальный ключ

def test_get_max_dict_key():
    menu_dict = {1: 'Option 1', 2: 'Option 2', 3: 'Option 3'}
    result = get_max_dict_key(menu_dict)
    assert result == 3  # Максимальный ключ

def test_check_menu_item_valid():
    menu_item = 2
    menu_dict = {1: 'Option 1', 2: 'Option 2', 3: 'Option 3'}
    result = check_menu_item(menu_item, menu_dict)
    assert result is True  # Должен вернуть True для существующего элемента

def test_check_menu_item_invalid():
    menu_item = 4
    menu_dict = {1: 'Option 1', 2: 'Option 2', 3: 'Option 3'}
    result = check_menu_item(menu_item, menu_dict)
    assert result is False  # Должен вернуть False для несуществующего элемента

@patch('builtins.input', side_effect=['5'])
def test_get_digit(mock_input):
    result = get_digit('Введите число: ', 'Ошибка ввода')
    assert result == 5  # Проверяем, что возвращается правильное число

@patch('builtins.input', side_effect=['abc', '5'])
def test_get_digit_invalid_input(mock_input):
    result = get_digit('Введите число: ', 'Ошибка ввода')
    assert result == 5  # Проверяем, что после некорректного ввода возвращается правильное число

@patch('builtins.input', side_effect=['yes'])
def test_get_yes_no_yes(mock_input):
    result = get_yes_no('Вы согласны? (да/нет): ', 'Ошибка ввода')
    assert result is True  # Проверяем, что возвращается True для "да"

@patch('builtins.input', side_effect=['no'])
def test_get_yes_no_no(mock_input):
    result = get_yes_no('Вы согласны? (да/нет): ', 'Ошибка ввода')
    assert result is False  # Проверяем, что возвращается False для "нет"

@patch('builtins.input', side_effect=['Hello World'])
def test_input_lower(mock_input):
    result = input_lower('Введите текст: ')
    assert result == 'hello world'  # Проверяем, что текст возвращается в нижнем регистре

@patch('builtins.input', side_effect=[' Hello World '])
def test_input_capitalize(mock_input):
    result = input_capitalize('Введите текст: ')
    assert result == 'Hello world'  # Проверяем, что текст возвращается с заглавной буквы
