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

        browser.element(by.text("Архивировать")).click()
        browser.element("//button[text()='Архивировать']").click()
        time.sleep(4)