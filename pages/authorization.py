import time

from selene import browser, by, be, have
import allure

from pages.base_page import BasePage


class PageAuthorization(BasePage):
    button_login = browser.element('a[href="/login"]')
    input_field_username = browser.element(by.name('username'))
    input_field_password = browser.element(by.name('password'))
    button_submit = browser.element('button[type="submit"]')

    def open_page(self, url="https://taskitnow.ru"):
        with allure.step("https://taskitnow.ru/"):
            browser.open(url)
            time.sleep(3)
            # browser.element('(//*[@type="email"])[1]').should(be.visible)

    def authorization(self, username="nurkaalek@gmail.com", password='Exane.18'):
        with allure.step("авторизоваться"):
            self.button_login.click()
            self.input_field_username.type(username)
            self.input_field_password.type(password)
            self.button_submit.click()
            browser.element('//button[@class="HeaderProfile_profile__card__pg9Mf"]').should(be.clickable)

    def logout(self):
        with allure.step(f"разлогиниться"):
            self.click_on_text("Эксанэ Алекперова")
            self.click_on_text("Выйти")

    def add_birthday(self):
        with allure.step(f"добавление даты рождения"):
            self.click_on('//*[@id="root-header"]/div[3]/div/button/div/div')
            self.click_on_text("Профиль")
            self.click_on("//button[.//span[text()='10.07.1997 ']]")
            self.click_on("//button[contains(@class, 'Calendar_day__xh0IC') and text()='10']")
            self.click_on_text("OK")
            self.click_on_text("Сохранить")

    def language(self):
        with allure.step(f"смена языка"):
            self.click_on('//*[@id="root-header"]/div[3]/div/button/div/div')
            self.click_on_text("РУС")
            self.click_on_text("English")

    def theme(self):
        with allure.step(f"смена темы"):
            self.click_on('//*[@id="root-header"]/div[3]/div/button/div/div')
            self.click_on("//div[@class='Switch_switch__handle__lLova']")

page_authorization = PageAuthorization()
