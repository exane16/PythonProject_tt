from selene.api import browser
import allure
class BasePage:
    def click_on(self,lokator:str):
        with allure.step(f"кликнуть на {lokator}"):
            browser.element(lokator).click()



