import time
from pages.authorization import page_authorization
from pages.create_workspace import page_workspace
from selene.api import *
import allure

@allure.story("успешное создание пространства")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("смоук тестирование")
@allure.title("тест создания пространства")
@allure.feature('пространство')
def test_authorization():
        page_authorization.open_page()
        page_authorization.authorization()
        page_workspace.workspace()

