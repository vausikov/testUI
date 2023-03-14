import time
import pytest
from helpers import ADBCommands
from selenium.common import NoSuchElementException
from pages import AndroidSettings


class TestBuildNumber:

    settings = AndroidSettings()

    # TODO:
    #   1: Выключать жесты на 13м андроиде перед тестами
    #   2: Каждый раз, когда происходит переход на друго активити,
    #  идет проверка на то, что оно действительно открылось. Необходимо как то подумать над вложенностью проверок

    def test_build_number(self):
        """
            Тест проверяет Номер сборки, отображающийся в UI гугловских настроек и сравнивает его
            со значением из системного проперти ro.build.id
        """
        try:
            if self.settings.driver.current_activity == self.settings.capabilities.get('appActivity'):
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