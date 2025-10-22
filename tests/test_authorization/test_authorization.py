from pages.authorization import page_authorization
import pytest
from pages.base_page import BasePage
import allure


# @pytest.fail
# @pytest.skip
@pytest.mark.regress
@allure.story("успешный логин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("смоук тестирование")
@allure.title("тест авторизации")
@allure.feature('авторизация')
def test_authorization():
    page_authorization.open_page()
    page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
