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

    browser.element("//*[@id='root-main']/div/button").click()
    browser.element("//input[@name='title' and @placeholder='Введите название' and @aria-required='true']").type('Тестирование')
    browser.element("//span[@data-color='false']").click()
    browser.element("//div[@aria-label='Color']").click()
    browser.element(by.text('Создать')).click()
    time.sleep(3)

    browser.element('//*[@id="root-main"]/div/div[4]/div/div/div[1]/div[2]/button[3]').click()
    browser.element(by.text('Удалить колонку')).click()
    browser.element(by.text('Удалить')).click()
    time.sleep(2)

