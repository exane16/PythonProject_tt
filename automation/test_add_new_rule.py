import time

from selene.core.match import browser_has_title

from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element('//*[@id="root-header"]/div[2]/button').click()
        browser.element(by.text("Автоматизация")).click()
        browser.element(by.text("Добавить новое правило")).click()
        browser.element("//input[@class='Checkbox_checkbox__field__IgG_I']").click()
        browser.element(by.text("Продолжить")).click()
        browser.element("//input[@class='Checkbox_checkbox__field__IgG_I']").click()
        browser.element(by.text("Продолжить")).click()
        browser.element(by.text("Сохранить")).click()
        time.sleep(2)
