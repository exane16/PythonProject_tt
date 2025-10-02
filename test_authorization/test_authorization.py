import time

import pytest

from pages.authorization import page_authorization
from selene.api import *
import allure
# @pytest.fail
# @pytest.skip
@pytest.mark.regress
@allure.story("успешный логин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("смоук тестирование")
@allure.title("тест авторизации")
@allure.feature('авторизация')
def test_tt():
    page_authorization.open_page()
    page_authorization.authorization()


