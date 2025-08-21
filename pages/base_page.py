from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.default_timeout = timeout

    def wait_for_element_visible(self, locator, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        else:
            timeout = timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"El elemento {locator} no fue visible tras {timeout} segundos")

    def find_element(self, locator, timeout=None):
        return self.wait_for_element_visible(locator, timeout)

    def click_element(self, locator, timeout=None):
        elemento = self.find_element(locator, timeout)
        elemento.click()

    def type_text(self, locator, texto, timeout=None):
        elemento = self.find_element(locator, timeout)
        elemento.clear()
        elemento.send_keys(texto)

    def get_text(self, locator, timeout=None):
        elemento = self.find_element(locator, timeout)
        return elemento.text

    def select_option(self, locator, value,timeout=None):
        select = Select(self.find_element(locator, timeout))
        select.select_by_value(value)

    def select_option_by_text(self, locator, text, timeout=None):
        select = Select(self.find_element(locator, timeout))
        select.select_by_visible_text(text)

    def select_option_by_index(self, locator, index, timeout=None):
        select = Select(self.find_element(locator, timeout))
        select.select_by_index(index)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=None):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False