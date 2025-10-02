import time

from selene.core.match import browser_has_title

from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element('//*[@id="root-header"]/div[2]/button').click()
        browser.element(by.text("Кастомные поля")).click()
        browser.element(by.text("Добавить поле")).click()
        browser.element("//button[@role='combobox']").click()
        browser.element(by.text("Число")).click()
        browser.element("//input[@placeholder='Введите название']").type("тест")
        browser.element("//div[@style='background-color: var(--color-additional-blue);']").click()
        browser.element("//p[text()='Дополнительные настройки']").click()
        browser.element('//*[@id="advanced-settings"]/div/div/div/div[4]/label[2]/input').type("55")
        browser.element(by.text("Добавить")).click()
        time.sleep(3)
        #browser.element("//ul[@class='some-class']//li//div[2]/button[1]").click()
        browser.element("//div[./label[contains(text(), 'Пользовательские поля')]]//button[contains(@class, 'Button_size_mid_only-icon__oRRGf')][1]").click()
        browser.element(by.text("Удалить")).click()
        time.sleep(4)

