from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class AndroidSettings(BasePage):

    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        appPackage='com.android.settings',
        appActivity='.Settings',
        noReset='false'
    )

    def __init__(self):
        super().__init__()

    def get_build_number(self):
        elements = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        for el in elements:
            index = elements.index(el)
            if el.get_attribute('text') == 'Номер сборки':
                build_number = index + 1
                return str(elements[build_number].get_attribute('text'))