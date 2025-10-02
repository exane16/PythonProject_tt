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

        browser.element("//p[@data-placeholder='Введите комментарий... \nВведите @, чтобы упомянуть и уведомить пользователя']").type("Написать автотесты")
        browser.element("//button[contains(@class, 'CommentField_field__button__qB_gN')]").click()
        time.sleep(4)

