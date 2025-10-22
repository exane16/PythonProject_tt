import time
from pages.authorization import page_authorization
from selene.api import *

from pages.create_workspace import page_workspace
from pages.base_page import BasePage

def test_create_workspace():
        page_authorization.open_page()
        page_authorization.authorization(username="nurkaalek@gmail.com", password='Exane.18')
        page_workspace.create_workspace()
        page_workspace.delete_workspace()
