from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base

class MainPage(Base):

    url = 'https://pitergsm.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    phone_link = '//li[@id="bx_651765591_1673"]'

    # Get elements
    # Get phone link.
    def get_phone_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_link)))

    # Action elements
    # Press phone link.
    def press_phone_link(self):
        self.get_phone_link().click()
        print('Phone link clicked.')

    # Methods
    def main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.press_phone_link()
