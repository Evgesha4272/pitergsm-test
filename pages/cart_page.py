from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price_phone = '//div[@id="basket_container"]/div[2]/div[1]/div/div[3]/div'
    btn_buy = '//div[@id="basket_container"]/div[2]/div[2]/div[2]/div[2]'

    # Get elements
    # Get price phone
    def get_price_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_phone)))

    # Get btn buy
    def get_btn_buy(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_buy)))


    # Action elements
    # Action btn by
    def click_btn_buy(self):
        self.get_btn_buy().click()
        print('We on conform page.')


    # Methods
    def cart_page(self):
        self.confirm_price(self.get_price_phone(), '27 190 руб.')
        self.click_btn_buy()
