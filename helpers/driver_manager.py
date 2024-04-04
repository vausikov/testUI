from appium import webdriver

class DriverManager:

    def __init__(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            appPackage='',
            appActivity='',
            noReset='false',
            newCommandTimeout=500
        )
        self.appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(self.appium_server_url, capabilities)