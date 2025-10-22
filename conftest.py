from webbrowser import Chrome
import os
import allure
import pytest
from selene.api import config,browser
@pytest.fixture(scope="function",autouse=True)
def browser_chrome(request):
    config.timeout=4
    config.window_height=1080
    config.window_width=1920
    config.reports_folder=("./reports")
    config.save_screenshot_on_failure = True
    config.save_page_source_on_failure = False
    yield browser
#         if os.path.exists(config.reports_folder):
#             files = os.listdir(config.reports_folder)
#             if len(files) > 0:
#                 with allure.step(f'Прикрепить скриншот'):
#                     request.addfinalizer(attach_screenshot_if_exists)
#         browser.quit()
#
# def attach_screenshot_if_exists():
#     """
#     Проверяет наличие скриншотов в папке отчетов и прикрепляет их к отчету.
#     """
#     try:
#         files = os.listdir(config.reports_folder)
#         png_files = [file for file in files if file.endswith('.png')]
#         if png_files:
#             newest_png = max(png_files, key=lambda x: os.path.getctime(os.path.join(config.reports_folder, x)))
#             screenshot_path = os.path.join(config.reports_folder, newest_png)
#             allure.attachments(screenshot_path)
#     except Exception as e:
#         error_message = f'Произошла ошибка при прикреплении скриншота\n{str(e)}'
#         with allure.step(error_message):
#             print(error_message)