import time
import pytest
from helpers import ADBCommands
from helpers.driver_manager import DriverManager
from selenium.common import NoSuchElementException
from pages import AndroidSettings


class TestBuildNumber:

    driver = DriverManager().driver
    driver.capabilities.update([('appPackage','com.android.settings'), ('appActivity', '.Settings')])
    settings = AndroidSettings(driver)

    def test_build_number(self):
        """
            Тест проверяет Номер сборки, отображающийся в UI гугловских настроек и сравнивает его
            со значением из системного проперти ro.build.id
        """
        self.driver.activate_app(self.driver.capabilities['appPackage'])
        try:
            if self.driver.current_activity == self.driver.capabilities.get('appActivity'):
                self.settings.swipe_to_element('О телефоне', duration=2000).click()
                time.sleep(1)
                if self.settings.driver.current_activity == '.SubSettings':
                    self.settings.swipe_to_element('Номер сборки', duration=2000)
                    ui_build_number = self.settings.get_build_number()
                    assert ui_build_number == ADBCommands.get_build_number()
                    self.settings.driver.quit()
                else:
                    pytest.fail('Activity was not open')
            else:
                pytest.fail('Activity was not open')
        except NoSuchElementException:
            pytest.fail('Swipe error. Element was not found')