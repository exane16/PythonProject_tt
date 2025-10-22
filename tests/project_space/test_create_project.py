from pages.authorization import page_authorization
from pages.project_page import project_page
from pages.base_page import BasePage

def test_create_project():
        # page_authorization.open_page()
        # page_authorization.authorization()
        # page_project.create_project()


        page_authorization.open_page(url="https://taskitnow.ru/")
        page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
        project_page.create_project(username="test 1")
