# coding=utf-8
""" Mock объекты для тестирования сайта https://ya.ru/"""


import pytest
import requests
import requests_mock


def mock_response():
    """ Mock ответ запроса сайта https://ya.ru/"""

    return requests.get("https://ya.ru/")

@pytest.fixture:
def mock():

    with requests_mock.Mocker() as mock_instance:
        yield mock_instance
