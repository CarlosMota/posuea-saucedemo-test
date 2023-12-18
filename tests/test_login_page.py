# test_login_page.py
from turtle import title
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        

    def tearDown(self):
        self.driver.quit()

    def test_login_to_saucedemo_valid(self):
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.do_login()
        
        products_page = ProductsPage(self.driver)

        title = products_page.get_product_page_title()

        # # Assert
        self.assertTrue("Products" in title.text)

    def test_login_to_saucedemo_invalid(self):
        # Arrange
        login_page = LoginPage(self.driver)

        # Act
        login_page.login(username="teste",password="teste")
        
        error_message = login_page.find_error_message()
        
        # # Assert
        self.assertTrue("Username and password do not match any user in this service" in error_message.text)


if __name__ == '__main__':
    unittest.main()
