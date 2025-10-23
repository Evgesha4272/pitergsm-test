from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base

class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    input_fio = '//input[@name="ORDER_PROP_1"]'
    input_email = '//input[@name="ORDER_PROP_2"]'
    input_phone = '//input[@name="ORDER_PROP_3"]'
    input_comment = '//textarea[@name="ORDER_DESCRIPTION"]'
    btn_make_order = '//button[@class="btn btn_cta"]'

    # Get elements
    # Get input fio
    def get_input_fio(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_fio)))

    # Get input email
    def get_input_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    # Get input phone
    def get_input_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    # Get input comment
    def get_input_comment(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_comment)))

    # Get btn make the order
    def get_btn_make_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_make_order)))


    # Action elements
    # Action input fio
    def put_input_fio(self):
        self.get_input_fio().send_keys('Antonov Anton Antonovich')
        print('Name was entered.')

    # Action input email
    def put_input_email(self):
        self.get_input_email().send_keys('super@gmail.com')
        print('Email was entered.')

    # Action input phone
    def put_input_phone(self):
        self.get_input_phone().send_keys('+79991233223')
        print('Phone was entered.')

    # Action input comment
    def put_input_comment(self):
        self.get_input_comment().send_keys('I am come in 15:00')
        print('Comment was entered.')

    # Action btn make the order
    def click_btn_make_order(self):
        self.get_btn_make_order().click()
        print('Order is made successfully.')

    # Methods
    def order_page(self):
        self.put_input_fio()
        self.put_input_email()
        self.put_input_phone()
        self.put_input_comment()
        self.click_btn_make_order()
