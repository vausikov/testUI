from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class AndroidSettings(BasePage):

    def get_build_number(self):
        #TODO:
        # Попробовать найти более лаконичный способ поиска значения Номера сборки, например переход к сестринскому
        # локатору. (Низкий приоритет)
        elements = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        for el in elements:
            index = elements.index(el)
            if el.get_attribute('text') == 'Номер сборки':
                build_number = index + 1
                return str(elements[build_number].get_attribute('text'))