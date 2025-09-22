import time

from selene.api import *

def test_tt():
    browser.open("https://taskitnow.ru")
    browser.element('a[href="/login"]').click()
    browser.element(by.name('username')).type('oalekperova.97@mail.ru')
    browser.element(by.name('password')).type('Exane.16')
    browser.element('button[type="submit"]').click()
    time.sleep(2)

    #browser.element('(//button)[2]').click()
    browser.element('//*[@id="root-main"]/div/button').click()
    browser.element("// input[ @ placeholder = 'Введите название']").type("test")
    browser.element(by.text("Создать")).click()

    time.sleep(6)

