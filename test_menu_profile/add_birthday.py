import time
from pages.authorization import page_authorization
from selene.api import *

def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()

        browser.element('button[type="submit"]').click()
        time.sleep(2)

        browser.element('//*[@id="root-header"]/div[3]/div/button/div/div').click()
        browser.element(by.text("Профиль")).click()
        browser.element(by.text("Выберите дату")).click()
        browser.element("//input[@placeholder='дд.мм.гггг' and @inputmode='decimal' and @pattern='[0-9.]*']").type("11.07.1997")
        browser.element(by.text("OK")).click()
        browser.element(by.text("Сохранить")).click()
        time.sleep(3)