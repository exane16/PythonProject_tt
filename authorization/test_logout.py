import time

from selene.api import *

def test_tt():
    browser.open("https://taskitnow.ru")
    browser.element('a[href="/login"]').click()
    browser.element(by.name('username')).type('nurkaalek@gmail.com')
    browser.element(by.name('password')).type('Exane.18')
    browser.element('button[type="submit"]').click()
    time.sleep(2)

    browser.element('//*[@id="root-header"]/div[3]/div/button/div/div').click()
    browser.element(by.text("Выйти")).click()
    time.sleep(3)