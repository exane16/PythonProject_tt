import time

from selene.api import *

def test_tt():
    browser.open("https://taskitnow.ru")
    browser.element('a[href="/login"]').click()
    browser.element(by.name('username')).type('nurkaalek@gmail.com')
    browser.element(by.name('password')).type('Exane.18')
    browser.element('button[type="submit"]').click()
    time.sleep(2)

    #browser.element('(//button)[2]').click()
    browser.element('/html/body/div/div[1]/aside/div/div[1]/div[2]/div/button').click()
    browser.element("// input[ @ placeholder = 'Введите название']").type("test 1")
    browser.element(by.text("Создать")).click()

    time.sleep(6)
