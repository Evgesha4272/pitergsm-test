from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base

class PhonePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_put_cart = '//div[@id="catalog"]/div[1]/div[3]/button'
    btn_ok = '//button[@id="cookie-consent-btn"]'
    btn_cart = '//div[@id="bx_basketFKauiI"]/div/div/a'

    # Get elements
    # Get btn put in cart
    def get_btn_put_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_put_cart)))

    # Get btn close pop-up
    def get_btn_ok(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_ok)))

    # Get btn cart
    def get_input_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_cart)))

    # Action elements
    # Action btn put in cart
    def press_btn_put_cart(self):
        self.get_btn_put_cart().click()
        print('Phone in cart.')

    # Action btn close pop-up
    def press_btn_ok(self):
        self.get_btn_ok().click()
        print('Pop-up is closed.')

    # Action btn cart
    def press_input_btn(self):
        self.get_input_btn().click()
        print('We are in cart.')

    # Methods
    def phone_page(self):
        self.press_btn_put_cart()
        self.driver.refresh()
        self.press_btn_ok()
        self.press_input_btn()
