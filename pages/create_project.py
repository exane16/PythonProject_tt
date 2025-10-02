from selene import browser, by
import allure

class PageProject:
    button_create_project = browser.element('/html/body/div/div[1]/aside/div/div[1]/div[2]/div/button')
    input_field_title = browser.element("// input[ @ placeholder = 'Введите название']")
    button_save_project = browser.element(by.text("Создать"))


    def project(self):
        with allure.step("создать проект"):
            self.button_create_project.click()
            self.input_field_title.type("test 1")
            self.button_save_project.click()


page_project = PageProject()