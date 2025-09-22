import time
from pages.authorization import PageAuthorization
from selene.api import *


def test_tt():
    PageAuthorization.open_page()
    PageAuthorization.authorization()
