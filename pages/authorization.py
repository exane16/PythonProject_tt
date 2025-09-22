from selene import browser, by


class PageAuthorization:

    button_login = browser.element('a[href="/login"]')
    input_field_username = browser.element(by.name('username')).type('nurkaalek@gmail.com')
    input_field_password = browser.element(by.name('password')).type('Exane.18')
    button_submit = browser.element('button[type="submit"]')
    @classmethod
    def open_page(cls):
        browser.open("https://taskitnow.ru")

    @classmethod
    def authorization(cls):
        cls.button_login.click()
        cls.input_field_username.type("nurkaalek@gmail.com")
        cls.input_field_password.type('Exane.18')
        cls.button_submit.click()
