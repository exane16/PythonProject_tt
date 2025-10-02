from selene import browser, by
import allure

class PageWorkspace:
    button_create_space = browser.element('//*[@id="root-main"]/div/button')
    input_field_title = browser.element("// input[ @ placeholder = 'Введите название']")
    button_save_space = browser.element(by.text("Создать"))



    def workspace(self):
        with allure.step("создать пространство"):
            self.button_create_space.click()
            self.input_field_title.type("test")
            self.button_save_space.click()


page_workspace = PageWorkspace()