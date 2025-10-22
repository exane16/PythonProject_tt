from selene import browser, by, be
import allure
from selene.common.data_structures.persistent import field
from pages.base_page import BasePage
import time

class PageTask(BasePage):
    button_create_task = browser.element("(//button[@title='Свернуть колонку']/following-sibling::button[.//*[contains(@class, 'Svg_icon__i_mPV')]])[1]")
    input_field_title = browser.element("//textarea[@name='title']")
    button_save_task = browser.element(by.text("Создать"))


    def create_task(self, username="test"):
        with allure.step("создать задачу"):
            self.button_create_task.click()
            self.input_field_title.type(username)
            self.button_save_task.click()
    def type_text_in_to_input_field(self, locator, text):
        element = browser.element(locator)
        element.should(be.visible)
        element.type(text)

    def add_comment(self, text="Написать автотесты"):
        with allure.step(f"добавление комментария"):
            self.type_text_in_to_input_field(
                locator="//p[@data-placeholder='Введите комментарий']",
                text= text)
            self.click_on("//button[contains(@class, 'CommentField_field__send') and @type='button']")

    def add_file(self):
        with allure.step(f"добавление вложения"):
            file_input = browser.element('input[type="file"]')
            file_input.send_keys(r"C:\Users\huawei\Desktop\i.webp")
            time.sleep(4)

    def arxiv_task(self):
        with allure.step(f"архивирование задачи"):
            self.click_on_text("Архивировать")
            self.click_on("//button[contains(text(), 'Архивировать')]")

    def connection_with_the_task(self, name="test 2"):
        with allure.step(f"связывание задачи"):

            self.click_on("(//button[contains(@class, 'Button_button__tElpV')])[22]")
            time.sleep(2)
            self.click_on("(//button[contains(@class, 'Button_button__tElpV')])[11]")
            time.sleep(2)
            self.type_text_in_to_input_field(
                locator="//textarea[@name='title']",
                text=name)
            self.click_on_text("Создать")
            self.click_on_text("Связывание")
            self.click_on("//button[contains(@class, 'RelationForm_relation__button__4p4Ya')]")
            time.sleep(2)
            self.click_on_text("Выберите задачу")
            time.sleep(1)
            self.click_on("//span[contains(@class, 'ActionItem_item__content__yKKyj')]")
            self.click_on("//button[text()='Отменить']/following-sibling::button[text()='Сохранить']")

    def copy_task(self, name="Копирование"):
        with allure.step(f"копирование задачи"):
            self.click_on_text("Копирование")
            self.type_text_in_to_input_field(
                locator="//input[@name='title']",
                text=name)
            self.click_on_text("Создать")

    def delete_task(self):
        with allure.step(f"удаление задачи"):
            self.click_on_text("Удалить")
            self.click_on_text("Подтвердить")

    def editing_task(self, name="Протестировать"):
        with allure.step(f"редактирование задачи"):
            time.sleep(2)
            self.click_on("//button[contains(text(), 'Выбрать теги')]//*[contains(@class, 'Svg_icon__i_mPV')]")
            time.sleep(2)
            self.click_on("//div[contains(@class, 'Tag_tag__38NN7') and contains(@class, 'Tag_tag_fill__85l5B')]")
            self.click_on('//*[@id="popover-header"]/button')
            self.click_on_text("Выбрать")
            self.click_on_text("Низкий")
            self.click_on_text("Назначить")
            self.click_on("//button[@role='option'  and contains(., 'Эксанэ Алекперова')]")
            self.click_on_text("Срок задачи | Мероприятие")
            self.click_on_text("Выберите дату")
            self.click_on("//button[contains(@class, 'Calendar_day__xh0IC') and text()='25']")
            self.click_on("//button[text()='OK']")
            self.click_on(
                "//button[text()='Сбросить все']/following-sibling::button[text()='Сохранить' and contains(@class, 'Button_style_accent__EGlTl')]")
            self.type_text_in_to_input_field(
                locator="//div[@contenteditable='true' and contains(@class, 'tiptap')]",
                text=name)
            self.click_on("//button[text()='Сохранить']")


    def filters(self, username="test"):
        with allure.step(f"фильтры"):
            self.click_on("//button[.//*[contains(@class, 'Svg_icon__i_mPV')]][   preceding-sibling::button[contains(@class, 'TaskPopupTop_top__displayType__SL0kw')] ]")
            self.click_on_text("Фильтры")
            self.type_text_in_to_input_field(
                locator="//input[@placeholder='Введите название']",
                text=username)
            self.click_on_text("Приоритет")
            self.click_on_text("Низкий")

    def share_task(self):
        with allure.step(f"поделиться задачей"):
            self.click_on_text("Поделиться")
            self.click_on_text("Ссылка на карточку")

    def subscribe_task(self):
        with allure.step(f"подписаться на задачу"):
            self.click_on_text("Подписаться")

task_page = PageTask()