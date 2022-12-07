import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator)).click()
        time.sleep(0.5)

    def send_keys_to_element(self, locator, text):
        WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(locator)).send_keys(text)

    def get_attribute_from_element(self, locator, attributename):
       get_attribute_name = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(locator)).get_attribute(attributename)
       return get_attribute_name

    def get_text_from_element(self, locator):
        get_text = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator)).text
        return get_text

    def wait_until_page_load(self, locator):
        WebDriverWait(self.driver, 20).until_not(ec.visibility_of_element_located(locator))

    def hover_to_element(self, locator):
        action = ActionChains(self.driver)
        element_hover = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(locator))
        action.move_to_element(element_hover).perform()
        time.sleep(0.5)

