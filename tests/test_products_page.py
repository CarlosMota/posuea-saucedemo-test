from ast import Assert
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestProductsPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        

    def tearDown(self):
        print("product page tear down")
        self.driver.quit()

    
    def test_add_product_to_cart(self):
        
        self.login_page.do_login()

        products_page = ProductsPage(self.driver)

        cart = products_page.add_first_product_to_cart()

        self.assertTrue(cart.text == "1")


if __name__ == '__main__':
    unittest.main()
