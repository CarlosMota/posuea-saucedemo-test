import unittest

from ast import Assert
from pages.footer_page import FooterPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.about_page import AboutPage
from pages.cart_page import CartPage
from pages.footer_page import FooterPage
from pages.general import General
from pages.login_page import LoginPage
from pages.menu_wrap import MenuWrap
from pages.products_detail_page import ProductsDetailPage
from pages.products_page import ProductsPage

class TestProductsDetailPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.about_page = AboutPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.footer_page = FooterPage(self.driver)
        self.general = General(self.driver)
        self.login_page = LoginPage(self.driver)
        self.menu_wrap = MenuWrap(self.driver)
        self.product_detail_page = ProductsDetailPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        
    def tearDown(self):
        print("product page tear down")
        self.driver.quit()
    
    def test_remove_product_to_cart(self):
        self.login_page.do_login()
        self.products_page.select_first_item_to_see_detail()
        cart = self.general.add_product_to_cart()
        self.assertTrue(cart.text == "1")
        self.general.navegate_to_cart_page()
        self.general.remove_product_to_cart()
    
    def test_navegate_to_products_page(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        self.cart_page.navegate_to_products_page()
        items = self.products_page.get_product_page_title()
        self.assertTrue(items.text == 'Products')
        
    def test_navegate_to_checkout_page(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        self.cart_page.navegate_to_checkout_page()
        
    def test_menu(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        menu = self.menu_wrap.menu()
        self.assertTrue(menu['all_items'].text == 'All Items')
        self.assertTrue(menu['logout'].text == 'Logout')
        self.assertTrue(menu['about'].text == 'About')
        self.assertTrue(menu['reset'].text == 'Reset App State')
        
    def test_logout(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        self.menu_wrap.click_logout()
        title = self.login_page.find_login_title()
        self.assertTrue(title.text == 'Swag Labs')

    def test_about(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        self.menu_wrap.click_about()
        about = self.about_page.get_about_text()
        self.assertTrue(about.text == 'The Sauce Test Toolchain')
        
    def test_all_items(self):
        self.login_page.do_login()
        self.general.navegate_to_cart_page()
        self.menu_wrap.click_all_items()
        items = self.products_page.get_product_page_title()
        self.assertTrue(items.text == 'Products')
        
    def test_reset_app_state(self):
        self.login_page.do_login()
        cart = self.general.add_product_to_cart()
        self.assertTrue(cart.text == "1")
        self.general.navegate_to_cart_page()
        self.menu_wrap.click_reset_app_state()