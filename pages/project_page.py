import time
from selene.api import browser
import allure
from selene.common.data_structures.persistent import field

from pages.base_page import BasePage


class PageProject(BasePage):
    def create_project(self, username="test"):
        with allure.step(f"создание проекта"):
            self.click_on("//p[contains(text(),'Проекты')]/following-sibling::button")
            self.type_text_in_to_input_field(
                lokator="//input[@name='title' and @placeholder='Введите название']",
                text=username)
            self.click_on("//button[@id='button-submit' and text()='Создать']")
            time.sleep(1)

    def check_create_project(self, name):
        self.check_text(name)
    def add_new_rule(self):
        with allure.step(f"создание нового правила"):
            self.click_on('//*[@id="root-header"]/div[2]/button')
            self.click_on_text("Автоматизация")
            self.click_on_text("Создать правило")
            self.click_on("//button[contains(@class, 'AutomationNew_table__btnCreate__5LNXY')][1]")
            self.click_on_text("Продолжить")
            self.click_on("//button[contains(text(),'Добавить')]")
            self.click_on("//*[contains(.,'с участниками')]/following::button[contains(@class, 'AutomationNew_table__btnCreate')][1]")
            self.click_on_text("Продолжить")
            self.click_on_text("Сохранить")

    def create_column(self,username='Тестирование'):
        with allure.step(f"создание колонки"):
            self.click_on("//button[contains(@class, 'TaskChangeColumn_create__UQ97J') and contains(@class, 'DashedButton_button__DAn6t') and contains(., '+ Добавить колонку')]")
            self.type_text_in_to_input_field(
                lokator="//input[@name='title' and @placeholder='Введите название' and @label='Название']",
                text=username)
            self.click_on_text('Создать')

    def delete_column(self, username="Тестирование"):
        with allure.step(f"Удаление колонки"):
            self.click_on("//*[@id='root-main']/div/button")
            self.type_text_in_to_input_field(
                lokator="//input[@name='title' and @placeholder='Введите название' and @aria-required='true']",
                text=username)
            self.click_on_text('Создать')
            self.click_on('//*[@id="root-main"]/div/div[4]/div/div/div[1]/div[2]/button[3]')
            self.click_on_text('Удалить колонку')
            self.click_on_text('Удалить')

    def add_custom_fields(self, username="тест", name="55", name_1="test"):
        with allure.step(f"создание кастомного поля"):
            self.click_on('//*[@id="root-header"]/div[2]/button')
            self.click_on_text("Кастомные поля")
            self.click_on_text("Добавить поле")
            self.click_on("//button[@role='combobox']")
            self.click_on_text("Число")
            self.type_text_in_to_input_field(
                lokator="//input[@placeholder='Введите название']",
                text=username)
            self.click_on("//div[@style='background-color: var(--color-additional-blue);']")
            self.click_on("//p[text()='Дополнительные настройки']")
            self.type_text_in_to_input_field(
                lokator='//*[@id="advanced-settings"]/div/div/div/div[4]/label[2]/input',
                text=name)
            self.click_on("//button[text()='Добавить']")
            self.click_on("//button[contains(@class, 'Modal_modal__btnClose__ReDuo')]")
            self.type_text_in_to_input_field(
                lokator='//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]',
                text=name_1)



    def delete_custom_fields(self, username="тест", name="55"):
        with allure.step(f"удаление кастомного поля"):
            self.click_on('//*[@id="root-header"]/div[2]/button')
            self.click_on_text("Кастомные поля")
            self.click_on_text("Добавить поле")
            self.click_on("//button[@role='combobox']")
            self.click_on_text("Число")
            self.type_text_in_to_input_field(
                lokator="//input[@placeholder='Введите название']",
                text=username)
            self.click_on("//div[@style='background-color: var(--color-additional-blue);']")
            self.click_on("//p[text()='Дополнительные настройки']")
            self.type_text_in_to_input_field(
                lokator='//*[@id="advanced-settings"]/div/div/div/div[4]/label[2]/input',
                text=name)
            self.click_on("//button[text()='Добавить']")
            self.click_on("//div[./label[contains(text(), 'Пользовательские поля')]]//button[contains(@class, 'Button_size_mid_only-icon__oRRGf')][1]")
            self.click_on_text("Удалить")

    def Exchange_Calendar(self, username="nurkaalek@gmail.com"):
        with allure.step(f"подключение Exchange Calendar"):
            self.click_on('//*[@id="root-header"]/div[2]/button')
            self.click_on_text("Подключения")
            self.click_on("//button[text()='Авторизоваться']")
            self.type_text_in_to_input_field(
                lokator="//input[@name='email']",
                text=username)
            self.click_on_text("Подключиться")

    def Git(self, url="https://gitlab.com"):
        with allure.step(f"подключение Git"):
            self.click_on('//*[@id="root-header"]/div[2]/button')
            self.click_on_text("Подключения")
            self.click_on("//a[text()='Git']")
            self.click_on("//button[contains(., 'Добавить подключение')]")
            self.type_text_in_to_input_field(
                lokator="//input[@name='url']",
                text=url)
            self.click_on_text("Подключиться")

    def invite_users(self, email="nurlaalek@gmail.com"):
        with allure.step(f"приглашение пользователя"):
            self.click_on("//button[contains(@class,'Button_button__tElpV') and normalize-space(text())='Пригласить']")
            self.type_text_in_to_input_field(
                lokator="//input[@name='invitedEmail']",
                text=email)
            self.click_on("//button[@id='w-submit']")

    def delete_users(self):
        with allure.step(f"удаление участника"):
            # self.click_on('id="modal-overlay" class="Overlay_overlay___AjbH')
            # self.click_on("//span[text()='Э']")
            self.click_on("(//div[contains(@class, 'Avatar_avatar__inner__YuSj2')])[1]")
            self.click_on_text("Удалить участника")
            self.click_on("//p[contains(@class, 'Typography_style_body___uqsc') and text()='Эксанэ Алекперова']/following-sibling::button[contains(@class, 'Button_size_mid_only-icon__oRRGf')]")
            self.click_on_text("Удалить")

    def browser_notifications(self):
        with allure.step(f"включение уведомлений в браузере"):
            self.click_on('//*[@id="root-header"]/div[3]/button[3]')
            self.click_on("//button[contains(@class, 'Button_button__tElpV') and contains(@class, 'Typography_style_label__gGacE')]")

    def delete_project(self):
        with allure.step(f"удаление проекта"):
            self.click_on('//*[@id="root-header"]/div[2]/button/div')
            self.click_on("//button[.//span[text()='Настройки']]")
            self.click_on('//*[@id="root-main"]/div/div[3]/button')
            self.click_on("//button[text()='Удалить']")

    def send_sms(self, username="test"):
        with allure.step(f"отправка смс"):
            self.click_on_text("Помощь")
            self.type_text_in_to_input_field(
                lokator="//textarea[@placeholder='Задайте нам вопрос, чтобы начать']",
                text=username)
            self.click_on("//button[@type='button' and contains(@class, 'Button_style_accent')]")
    def send_file(self, field="test"):
        with allure.step(f"прикрепление файла в чат поддержки"):
            self.click_on_text("Помощь")
            self.type_text_in_to_input_field(
                lokator='textarea[placeholder="Задайте нам вопрос, чтобы начать"]',
                text=field)
            file_input = browser.element('input[type="file"]')
            file_input.send_keys("C:/Users\huawei\Desktop\i.webp")
            self.click_on("(//button[@type='button' and contains(@class, 'Button_style_accent')])[2]")


project_page=PageProject()