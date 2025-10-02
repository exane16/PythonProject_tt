import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element("//*[@id='root-main']/div/button").click()
        browser.element("//input[@name='title' and @placeholder='Введите название' and @aria-required='true']").type('Тестирование')
        browser.element("//button/span[@data-color='false']").click()
        browser.element("//div[@role='slider']").click()
        browser.element(by.text('Создать')).click()
        time.sleep(3)
