from urllib.parse import urlparse

from termcolor import colored

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://b2c.passport.rt.ru/')

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    # Найти элемент и кликнуть по нему
    def find_element_and_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Элемент {locator} не найден').click()

    # Проверить видимость элемента
    def is_visible(self, locator, time=5) -> bool:
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return element

    # Очистка поля ввода
    def clear(self, locator, text, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).clear()

    # Ввод данных
    def input_data(self, locator, text, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Получить атрибут текст элемента
    def get_text_of_element(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return element.text