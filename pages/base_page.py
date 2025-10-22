from selene.api import browser, be, by, have
import allure
class BasePage:
    def open_page(self,url):
        with allure.step(f"открытие страницы '{url}'"):
            browser.open(url)
    def click_on(self,lokator:str):
        with allure.step(f"кликнуть на {lokator}"):
            browser.element(lokator).click()
    def check_element_is_clikable(self, lokator:str):
        with allure.step(f"проверить, что элемент {lokator} кликабелен"):
            browser.element(lokator).should(be.clickable)
    def type_text_in_to_input_field(self,lokator,text):
        with allure.step(f"ввести текст '{text}' в поле ввода"):
            browser.element(lokator).type(text)
    def check_text(self,text):
            with allure.step(f"проверка на наличие текста  '{text}'"):
                browser.element(by.partial_text(text)).should(be.visible)
    def click_on_text(self,text):
            with allure.step(f"клик на текст '{text}'"):
                browser.element(by.partial_text(text)).click()



