import time
from appium.webdriver.common.appiumby import AppiumBy
from pages import AndroidSettings


class TestWiFi:

    settings = AndroidSettings()

    def test_switch_on(self):
        """
            Кейс:
                Подключение к вай-фай с заранее сохраненной точкой доступа
            Критерий приемки:
                Проверить значек в шторке
                В настройках отображается "Подключено"
                Выдался айпишник и мак адрес
        """
        self.settings.swipe_to_element('Сеть и интернет', 2000).click()
        time.sleep(1)
        self.settings.swipe_to_element('Интернет', 2000).click()
        time.sleep(1)
        self.settings.driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Switch').click()
        time.sleep(10)
        sb = self.settings.driver.get_system_bars().get('statusBar')
        self.settings.driver.swipe(500, 50, 500, 550, 500)