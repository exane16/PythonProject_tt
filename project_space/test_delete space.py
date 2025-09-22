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
    browser.element('//*[@id="root-main"]/div/button').click()
    browser.element("// input[ @ placeholder = 'Введите название']").type("test")
    browser.element(by.text("Создать")).click()

    browser.element('//*[@id="root-main"]/div/div[2]/a[4]').click()
    browser.element('//*[@id="root-main"]/div/div[3]/div/div[3]/button').click()
    time.sleep(2)
    browser.element(by.text("Удалить")).click()
    time.sleep(4)