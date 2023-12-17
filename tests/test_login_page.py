# test_login_page.py
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

    def test_login_to_saucedemo(self):
        # Arrange
        login_page = LoginPage(self.driver)

        #credentials
        credentials = login_page.load_credentials()

        # Act
        login_page.login(username=credentials["username"],password=credentials["password"])
        
        products_page = ProductsPage(self.driver)
        # # Assert
        self.assertTrue("Products" in products_page.products_title.text)


if __name__ == '__main__':
    unittest.main()
