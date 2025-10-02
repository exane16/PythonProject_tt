import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project
from pages.create_task import page_task


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()
        page_task.task()

        browser.element("//button[contains(@class, 'TaskPopupTop_top__close__mXf8P')]").click()
        time.sleep(1)
        browser.element('//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]').click()
        browser.element("//textarea[@name='title']").type("test 2")
        browser.element(by.text("Создать")).click()
        browser.element("//button[contains(@class, 'TaskPopupTop_top__close__mXf8P')]").click()
        time.sleep(1)
        browser.element("//div[contains(@class, 'Board_card_main__xieKh')]").click()
        browser.element(by.text("Связывание")).click()
        browser.element(by.text("Добавить новую связь")).click()
        browser.element(by.text("Выберите задачу")).click()
        browser.element("//button[.//span[text()='test 2']]").click()
        time.sleep(3)
        browser.element("//button[text()='Отменить']/following-sibling::button[text()='Сохранить']").click()
        time.sleep(4)