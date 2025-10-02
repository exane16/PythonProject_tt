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

        browser.element(by.text("Выбрать")).click()
        browser.element(by.text("Низкий")).click()
        browser.element(by.text("Назначить")).click()
        browser.element("//button[@role='option'  and contains(., 'Эксанэ Алекперова')]").click()
        time.sleep(2)
        browser.element("//button[contains(@class, 'TaskPopupTop_top__close__mXf8P')]").click()
        time.sleep(1)
        browser.element(by.text("Фильтры")).click()
        browser.element("//input[@placeholder='Введите название']").type("test")
        browser.element("//button[@class='Avatar_avatar__wtyKS' and @data-state='closed']").click()
        browser.element(by.text("Приоритет")).click()
        browser.element(by.text("Низкий")).click()
        time.sleep(1)