from selene import browser, by
import allure

class PageTask:
    button_create_task = browser.element('//*[@id="root-main"]/div/div[1]/div/div/div[1]/div[2]/button[2]')
    input_field_title = browser.element("//textarea[@name='title']")
    button_save_task = browser.element(by.text("Создать"))


    def task(self):
        with allure.step("создать задачу"):
            self.button_create_task.click()
            self.input_field_title.type("test")
            self.button_save_task.click()


page_task = PageTask()