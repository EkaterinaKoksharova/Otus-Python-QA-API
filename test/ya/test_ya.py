""" Тесты сайта https://ya.ru/ """


import requests
from test.ya.mock import mock, mock_response


class TestYaSite:
    """ Тесты сайта https://ya.ru/ """

    def test_ya_1(self, url_param, status_code_param):
        """ Проверка работы параметров --url и --status_code """
        response = requests.get(url_param)
        assert response.status_code == status_code_param

    def test_ya_mock(self, mock):
        """ Проверка ответа с mock"""

        mock.get("https://ya.ru/", status_code=500)
        response = mock_response()

        assert response.status_code == 500
