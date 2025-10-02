import time
from pages.authorization import page_authorization
from selene.api import *

def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()

        browser.element('button[type="submit"]').click()
        time.sleep(2)

        browser.element('//*[@id="root-header"]/div[3]/div/button/div/div').click()
        browser.element(by.text("РУС")).click()
        browser.element(by.text("English")).click()
        time.sleep(4)