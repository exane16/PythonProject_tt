import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element("//button[contains(@class, 'Button_button__tElpV') and normalize-space(text())='Пригласить']").click()
        browser.element('input[name="invitedEmail"]').type("oalekperova.1997@mail.ru")
        browser.element(by.text("Отправить")).click()
        time.sleep(4)