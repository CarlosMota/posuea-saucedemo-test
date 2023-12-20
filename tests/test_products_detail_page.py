from ast import Assert
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.products_detail_page import ProductsDetailPage
from pages.about_page import AboutPage

class TestProductsDetailPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_detail_page = ProductsDetailPage(self.driver)
        self.about_page = AboutPage(self.driver)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_add_product_to_cart(self):
        self.login_page.do_login()
        self.products_page.select_first_item_to_see_detail()
        cart = self.product_detail_page.add_product_to_cart()
        self.assertTrue(cart.text == "1")
        
    def test_navegate_to_products_page(self):
        self.login_page.do_login()
        self.products_page.select_first_item_to_see_detail()
        self.product_detail_page.navegate_to_products_page()
        
    def test_navigate_from_products_to_cart(self):
        self.login_page.do_login()
        self.products_page.select_first_item_to_see_detail()
        cart = self.product_detail_page.add_product_to_cart()
        cart.click()
        cart_button = self.cart_page.get_cart_title()
        self.assertTrue(cart_button.text == 'Your Cart')

    def test_menu(self):
        self.login_page.do_login()
        menu = self.product_detail_page.menu()
        self.assertTrue(menu['all_items'].text == 'All Items')
        self.assertTrue(menu['logout'].text == 'Logout')
        self.assertTrue(menu['about'].text == 'About')
        self.assertTrue(menu['reset'].text == 'Reset App State')
        
    def test_logout(self):
        self.login_page.do_login()
        self.product_detail_page.logout()
        title = self.login_page.find_login_title()
        self.assertTrue(title.text == 'Swag Labs')

    def test_about(self):
        self.login_page.do_login()
        self.product_detail_page.about()
        about = self.about_page.get_about_text()
        self.assertTrue(about.text == 'The Sauce Test Toolchain')