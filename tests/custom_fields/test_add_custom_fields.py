import time

from selene.core.match import browser_has_title

from pages.authorization import page_authorization
from selene.api import *
from pages.project_page import project_page
from pages.base_page import BasePage

def test_create_project():
        page_authorization.open_page()
        page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
        project_page.create_project()
        project_page.add_custom_fields()
