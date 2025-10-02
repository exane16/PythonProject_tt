import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_workspace import page_workspace


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_workspace.workspace()

        browser.element('//*[@id="root-main"]/div/div[2]/a[4]').click()
        browser.element('//*[@id="root-main"]/div/div[3]/div/div[3]/button').click()
        time.sleep(2)
        browser.element(by.text("Удалить")).click()
        time.sleep(2)