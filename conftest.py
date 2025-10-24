import os
import allure
import pytest
from selene.api import config, browser


@pytest.fixture(scope="function", autouse=True)
def browser_chrome(request):
    config.timeout = 4
    config.window_height = 1080
    config.window_width = 1920
    config.reports_folder = "./reports"
    config.save_screenshot_on_failure = True
    config.save_page_source_on_failure = False

    yield browser

    # регистрируем финализатор только если есть файлы
    if os.path.exists(config.reports_folder):
        files = os.listdir(config.reports_folder)
        if any(f.endswith('.png') for f in files):
            request.addfinalizer(attach_screenshot_if_exists)


def attach_screenshot_if_exists():
    """Проверяет наличие скриншотов в папке отчетов и прикрепляет их к отчету."""
    try:
        files = [f for f in os.listdir(config.reports_folder) if f.endswith('.png')]
        if files:
            newest_png = max(
                files,
                key=lambda f: os.path.getctime(os.path.join(config.reports_folder, f))
            )
            screenshot_path = os.path.join(config.reports_folder, newest_png)
            allure.attach.file(
                screenshot_path,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        error_message = f'Произошла ошибка при прикреплении скриншота: {e}'
        with allure.step(error_message):
            print(error_message)



