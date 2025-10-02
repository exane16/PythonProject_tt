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
        time.sleep(2)
        browser.element(by.text("Добавить")).click()
        browser.element("//button[contains(@class, 'Modal_modal__btnClose__ReDuo')]").click()
        time.sleep(2)
        browser.element('//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]').click()
        browser.element("//textarea[@name='title']").type("test")
        browser.element(by.text("Создать")).click()
        time.sleep(4)