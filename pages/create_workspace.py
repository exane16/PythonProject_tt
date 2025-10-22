from selene import browser, by
import allure
from pages.base_page import BasePage
class PageWorkspace:
    button_create_space = browser.element('//*[@id="root-main"]/div/button')
    input_field_title = browser.element("// input[ @ placeholder = 'Введите название']")
    button_save_space = browser.element(by.text("Создать"))
    button_delete_space = browser.element('//*[@id="root-main"]/div/div[2]/a[4]')
    button_delete_space_2 = browser.element('//*[@id="root-main"]/div/div[3]/div/div[3]/button')
    button_delete_space_3 = browser.element(by.text("Удалить"))

    def create_workspace(self):
        with allure.step("создать пространство"):
            self.button_create_space.click()
            self.input_field_title.type("test")
            self.button_save_space.click()

    def delete_workspace(self):
        with allure.step(f"удаление пространства"):
            self.button_delete_space.click()
            self.button_delete_space_2.click()
            self.button_delete_space_3.click()



page_workspace = PageWorkspace()