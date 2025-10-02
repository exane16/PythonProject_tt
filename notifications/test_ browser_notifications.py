import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_project import page_project


def test_tt():
        page_authorization.open_page()
        page_authorization.authorization()
        page_project.project()

        browser.element('//*[@id="root-header"]/div[3]/button[3]').click()
        browser.element("//button[contains(@class, 'Button_button__tElpV') and contains(@class, 'Typography_style_label__gGacE')]").click()
        time.sleep(5)