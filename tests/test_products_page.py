from ast import Assert
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CkeckoutPage

class TestProductsPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.checkout_page = CkeckoutPage(self.driver)

    def tearDown(self):
        print("product page tear down")
        self.driver.quit()

    
    def test_add_product_to_cart(self):
        
        self.login_page.do_login()

        cart = self.products_page.add_first_product_to_cart()

        self.assertTrue(cart.text == "1")

    def test_sort_product_to_az(self):

        self.login_page.do_login()

        first_product = self.products_page.sort_products_to_az()

        self.assertTrue(first_product == "Sauce Labs Backpack")

    def test_sort_product_to_za(self):

        self.login_page.do_login()

        first_product = self.products_page.sort_products_to_za()

        self.assertTrue(first_product == "Test.allTheThings() T-Shirt (Red)")


    def test_sort_product_to_low_to_high(self):

        self.login_page.do_login()

        first_product = self.products_page.sort_products_to_low_to_high()

        self.assertTrue(first_product == "Sauce Labs Onesie")

    def test_sort_product_to_high_to_low(self):

        self.login_page.do_login()

        first_product = self.products_page.sort_products_to_high_to_low()

        self.assertTrue(first_product == "Sauce Labs Fleece Jacket")

    def test_navigate_from_products_to_checkout(self):

        self.login_page.do_login()

        cart = self.products_page.add_first_product_to_cart()

        cart.click()

        checkout_button = self.checkout_page.get_checkout_button()

        self.assertTrue(checkout_button.text == 'Checkout')

        

if __name__ == '__main__':
    unittest.main()
