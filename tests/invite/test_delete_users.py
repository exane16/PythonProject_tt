import time
from pages.authorization import page_authorization
from selene.api import *
from pages.base_page import BasePage
from pages.project_page import project_page

def test_create_project():
        page_authorization.open_page()
        page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
        # page_project.create_project()
        project_page.create_project()
        project_page.invite_users()
        project_page.delete_users()
