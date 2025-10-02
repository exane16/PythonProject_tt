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
        time.sleep(2)
        browser.element(by.text("Выбрать теги")).click()
        browser.element("//input[@class='Checkbox_checkbox__field__IgG_I']").click()
        browser.element('//*[@id="popover-header"]/button').click()
        time.sleep(1)
        browser.element(by.text("Выбрать")).click()
        browser.element(by.text("Низкий")).click()
        browser.element(by.text("Назначить")).click()
        browser.element("//button[@role='option'  and contains(., 'Эксанэ Алекперова')]").click()
        #browser.element('//input[@class="Checkbox_checkbox__field__IgG_I"]').click()
        browser.element(by.text("Срок задачи | Мероприятие")).click()
        browser.element(by.text("Выберите дату")).click()
        time.sleep(2)
        browser.element("//button[contains(@class, 'Calendar_day__xh0IC') and text()='25']").click()
        time.sleep(2)
        browser.element("//button[text()='OK']").click()
        browser.element("//button[text()='Сбросить все']/following-sibling::button[text()='Сохранить' and contains(@class, 'Button_style_accent__EGlTl')]").click()
        time.sleep(2)
        browser.element("//div[@contenteditable='true' and contains(@class, 'tiptap')]").type('Протестировать')
        browser.element("//button[text()='Сохранить']").click()
        time.sleep(2)
        browser.element("//button[contains(@class, 'TaskPopupTop_top__close__mXf8P')]").click()
        time.sleep(5)

