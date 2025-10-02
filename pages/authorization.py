from selene import browser, by
import allure

class PageAuthorization:
    button_login = browser.element('a[href="/login"]')
    input_field_username = browser.element(by.name('username'))
    input_field_password = browser.element(by.name('password'))
    button_submit = browser.element('button[type="submit"]')

    def open_page(self):
        with allure.step("https://taskitnow.ru/"):
            browser.open("https://taskitnow.ru")
            #browser.element('id="root-main').should(be.visible)

    def authorization(self):
        with allure.step("авторизоваться"):
            self.button_login.click()
            self.input_field_username.type("nurkaalek@gmail.com")
            self.input_field_password.type('Exane.18')
            self.button_submit.click()


page_authorization = PageAuthorization()
