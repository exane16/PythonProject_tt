import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element(by.text("Помощь")).click()
        browser.element("//textarea[@placeholder='Задайте нам вопрос, чтобы начать']").type("test")
        browser.element("//button[@type='button' and contains(@class, 'Button_style_accent')]").click()
        time.sleep(2)