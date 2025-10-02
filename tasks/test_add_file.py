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

        #fle_path = Path('tests/data/my_file.png').resolve()
        time.sleep(4)
        browser.element('input[type="file"]').send_keys("C:/Users\huawei\Desktop/nature-landscape-mountains-obersee-lake-Germany-trees-dead-trees-2286330.jpg")
        time.sleep(4)
