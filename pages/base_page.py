import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator)).click()

    def js_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator)).send_keys(
            text)

    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator)).text

    def switch_to_new_window(self, old_windows, timeout=10):
        start_time = time.time()
        while len(self.driver.window_handles) <= len(old_windows):
            if time.time() - start_time > timeout:
                raise TimeoutError("Новое окно не открылось за отведенное время")
            time.sleep(0.3)
        new_windows = [w for w in self.driver.window_handles if w not in old_windows]
        self.driver.switch_to.window(new_windows[0])
