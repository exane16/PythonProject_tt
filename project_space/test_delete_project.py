import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element('//*[@id="root-header"]/div[2]/button/div').click()
        time.sleep(2)
        browser.element("//button[.//span[text()='Настройки']]").click()
        time.sleep(3)
        browser.element('//*[@id="root-main"]/div/div[3]/button').click()
        time.sleep(2)
        browser.element(by.text("Удалить")).click()
        time.sleep(4)
