from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AppDriver:
    def __init__(self):
        self.app_url = "https://caesarspalaceonline.com/us/nj/casino"
        self.driver = self.configure_driver()

    def configure_driver(self):
        options = Options()
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--verbose")
        driver = webdriver.Chrome(options=options)
        driver.get(self.app_url)
        return driver

    def click_element(self, locator):
        """
        custom wrapped click method
        -> wait for element until display and clicks
        -> element(s)
        """
        try:
            element = self.create_element(locator)
            if element != None:
                element.click()
        except TimeoutException:
            assert False, f'Element not found/timeout exception" ' + str(locator)

    def is_exist(self, locator, expected=True, n=5, **kwargs):
        """
        returns boolean value by polling if match is not found or not
        maximum poll #3 with approx. ~10 secs
        """
        while n > 0:
            try:
                if len(kwargs) == 0 and self.driver.find_element(*locator).is_displayed() == expected:
                    return True
                elif self.driver.find_elements(*locator)[kwargs['index']].is_displayed() == expected:
                    return True
            except Exception as e:
                n -= 1
                time.sleep(0.5)
                if n == 0: return False

    def send_keys(self, locator, text=''):
        """
        custom wrapped send keys method
        -> wait for element until display and input
        -> element(s)
        """
        try:
            element = self.create_element(locator)
            if element != None:
                element.clear()
                element.send_keys(text)
        except TimeoutException:
            assert False, f'Element not found/timeout exception. Locator:' + str(locator)

    def create_element(self, locator):
        """
        Create element if it appears
        :param locator:
        :return: WebElement
        """
        is_element = self.wait_until_appear(locator)
        if is_element:
            return self.driver.find_element(*locator)
        else:
            return None

    def wait_until_appear(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            return False