import time

from selene.api import *

def test_tt():
    browser.open("https://taskitnow.ru")
    browser.element('a[href="/login"]').click()
    browser.element(by.name('username')).type('nurkaalek@gmail.com')
    browser.element(by.name('password')).type('Exane.18')
    browser.element('button[type="submit"]').click()
    time.sleep(2)

    browser.element('/html/body/div/div[1]/aside/div/div[1]/div[2]/div/button').click()
    browser.element("//input[@name='title']").type("test")
    browser.element(by.text("Создать")).click()
    time.sleep(3)
    browser.element('//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]').click()
    browser.element("//textarea[@name='title']").type("test")
    browser.element(by.text("Создать")).click()
    browser.element(by.text("Выбрать")).click()
    browser.element(by.text("Низкий")).click()
    browser.element(by.text("Назначить")).click()
    browser.element('//input[@class="Checkbox_checkbox__field__IgG_I"]').click()
    time.sleep(2)
    browser.element("//button[contains(@class, 'TaskPopupTop_top__close__mXf8P')]").click()
    time.sleep(1)
    browser.element(by.text("Фильтры")).click()
    browser.element("//input[@placeholder='Введите название']").type("test")
    browser.element("//button[@class='Avatar_avatar__wtyKS' and @data-state='closed']").click()
    browser.element(by.text("Приоритет")).click()
    browser.element(by.text("Низкий")).click()
    time.sleep(1)