import pytest
from src.driver import AppDriver
from src.screens.login_screen import LoginScreen


@pytest.fixture(scope='function')
def app():
    return AppDriver()


@pytest.fixture(scope='function')
def login_screen(app):
    return LoginScreen(app)
