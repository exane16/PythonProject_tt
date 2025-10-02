import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element('//*[@id="root-header"]/div[2]/button').click()
        browser.element(by.text("Подключения")).click()
        browser.element("//button[text()='Авторизоваться']").click()
        browser.element("//input[@name='email']").type("nurkaalek@gmail.com")
        browser.element(by.text("Подключиться")).click()
        time.sleep(2)