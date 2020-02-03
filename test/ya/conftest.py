""" Фикстуры и параметры тестов сайта https://ya.ru/ """

import pytest

def pytest_addoption(parser):
    """ Парамтры, которые можно передавать при запуске тестов из терминала."""
    parser.addoption("--url",
                     default="https://ya.ru",
                     help="This is request url")
    parser.addoption("--status_code",
                     action='store',
                     default=200,
                     help="This is expected request status",
                     type=int)

@pytest.fixture
def url_param(request):
    """ Значание параметра --url, переданного в команде pytest """
    return request.config.getoption('--url')

@pytest.fixture
def status_code_param(request):
    """ Значание параметра --status_code, переданного в команде pytest """
    return request.config.getoption('--status_code')
