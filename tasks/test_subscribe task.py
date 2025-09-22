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

    browser.element('//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]').click()
    browser.element("//textarea[@name='title']").type("test")
    browser.element(by.text("Создать")).click()
    browser.element(by.text("Подписаться")).click()
    time.sleep(2)