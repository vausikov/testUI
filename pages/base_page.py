from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, InvalidElementStateException


class BasePage:
    capabilities = dict(
        platformName='',
        automationName='',
        appPackage='',
        appActivity='',
    )

    appium_server_url = 'http://localhost:4723'

    def __init__(self):
        self.driver = webdriver.Remote(self.appium_server_url, self.capabilities)

    def swipe_to_element(self, text_attribute, duration=2500):
        last_element_on_screen = None
        previous_last_element_on_screen = None
        elements_list = None
        while True:
            previous_last_element_on_screen = last_element_on_screen
            try:
                elements_list = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.LinearLayout')
                last_element_on_screen = elements_list[-1]
                el = self.driver.find_element(AppiumBy.XPATH, '//*[@text="{0}"]'.format(text_attribute))
                # TODO:
                #   Иногда возникает ситуация, когда в одном элементе есть 2 или более TextView, например заголовок и значение,
                #   и при этом одно отображается, а другое нет. Лоика тестов такова, что, если найден заголовок,
                #   то можно и прочитать значение. Поэтому, нужно сделать так, чтобы элемент отображался целиком.
                return el
            except NoSuchElementException:
                self.swipe_list(elements_list, duration)
                if previous_last_element_on_screen == last_element_on_screen:
                    raise NoSuchElementException

    # TODO:
    #  swipe_list пропускает элементы, если он слишком быстрый. Чем мельче элементы, значит их больше отображаеся на
    #  экране, тем выше шанс пропуска.
    #  Возможное решение:
    #       1й вариант: Считать кол-во отображаемых элементов. Отслеживать
    #  аттрибут @displayed. Прекращать свайп когда все элементы скроются, кроме последнего.
    #       2й вариант: ...

    def swipe_list(self, elements_list, duration):
        try:
            first_element_location = elements_list[1].location
            target_element_location = elements_list[-1].location
            self.driver.swipe(target_element_location['x'], target_element_location['y'],
                              first_element_location['x'], first_element_location['y'], duration)
        except InvalidElementStateException:
            print('The swipe action was not performed')
            pass
