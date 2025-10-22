import time
from pages.authorization import page_authorization
from selene.api import *
from pages.base_page import BasePage

def test_authorization():
        page_authorization.open_page()
        page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
        page_authorization.theme()
