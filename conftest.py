from webbrowser import Chrome

import pytest
from selene.api import config,browser
@pytest.fixture(scope="function",autouse=True)
def browser_chrome():
    config.timeout=4
    config.window_height=1080
    config.window_width=1920
    yield browser
    browser.quit()
    config.reports_folder=("./reports")
    config.save_screenshot_on_failure=True
    config.save_page_source_on_failure=False