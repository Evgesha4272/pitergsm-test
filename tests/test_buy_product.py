import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.phone_page import PhonePage


def test_buy_product(set_up):
    # Settings for browser open.
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(options = options, service = g)

    print('Start test - 1.')

    # Call method main page
    main_p = MainPage(driver)
    main_p.main_page()

    # Call method phone page
    phone_p = PhonePage(driver)
    phone_p.phone_page()

    # Call method cart page
    cart_p = CartPage(driver)
    cart_p.cart_page()

    # Call method order page
    order_p = OrderPage(driver)
    order_p.order_page()

    time.sleep(2)
    driver.quit()

    print('Finish test - 1.')