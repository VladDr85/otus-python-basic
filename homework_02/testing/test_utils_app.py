import pytest
from homework_02.app.utils import utils_app as ut


class TestUtilsApp:
    dict_asc = {1: 'Значение 1',
                2: 'Значение 2',
                3: 'Значение 3',
                4: 'Значение 4'}

    dict_desc = {5: 'Значение 5',
                 4: 'Значение 4',
                 3: 'Значение 3',
                 2: 'Значение 2'}

    @pytest.mark.parametrize("test_dict, res",
                             [
                                 (dict_asc, 1),
                                 (dict_desc, 2),
                             ]
                             )
    def test_get_show_menu_item(self, test_dict, res):
        assert ut.get_show_menu_item(test_dict) == res

    @pytest.mark.parametrize("test_dict, res",
                             [
                                 (dict_asc, 4),
                                 (dict_desc, 5),
                             ]
                             )
    def test_get_max_dict_key(self, test_dict, res):
        assert ut.get_max_dict_key(test_dict) == res

    @pytest.mark.parametrize("menu_item, menu_dict, res",
                             [
                                 (1, dict_asc, True),
                                 (3, dict_asc, True),
                                 (8, dict_asc, False),
                             ]
                             )
    def test_check_menu_item(self, menu_item, menu_dict, res):
        assert ut.check_menu_item(menu_item, menu_dict) == res

    def test_get_digit(self):
        ut.input = lambda x: '1'
        assert ut.get_digit('Сообщение пользователю', 'Сообщение с ошибкой') == 1

    @pytest.mark.parametrize("input_data, res",
                             [
                                 ('Y', True),
                                 ('y', True),
                                 ('Yes', True),
                                 ('да', True),
                                 ('n', False),
                                 ('нет', False),
                                 ('no', False),
                                 ('N', False),
                             ]
                             )
    def test_get_yes_no(self, input_data, res):
        ut.input = lambda x: input_data
        assert ut.get_yes_no('Сообщение пользователю', 'Сообщение с ошибкой') == res

    @pytest.mark.parametrize("input_data, res",
                             [
                                 ('Some', 'some'),
                                 ('SOME', 'some'),
                                 (' Some ', 'some'),
                                 ('SomE ', 'some'),
                                 (' Some', 'some'),
                                 ('Some', 'some'),
                             ]
                             )
    def test_input_lower(self, monkeypatch, input_data, res):
        ut.input = lambda x: input_data
        assert ut.input_lower(input_data) == res

    @pytest.mark.parametrize("input_data, res",
                             [
                                 ('Some', 'Some'),
                                 ('SOME', 'Some'),
                                 (' Some ', 'Some'),
                                 ('SomE ', 'Some'),
                                 (' Some', 'Some'),
                                 ('Some', 'Some'),
                             ]
                             )
    def test_input_capitalize(self, monkeypatch, input_data, res):
        ut.input = lambda x: input_data
        assert ut.input_capitalize('Сообщение пользователю') == res
