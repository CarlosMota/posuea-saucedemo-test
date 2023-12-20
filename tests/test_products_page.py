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

class TestProductsPage(unittest.TestCase):
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

    def test_navigate_from_products_to_cart(self):
        self.login_page.do_login()
        cart = self.products_page.add_first_product_to_cart()
        cart.click()
        cart_button = self.cart_page.get_cart_title()
        self.assertTrue(cart_button.text == 'Your Cart')

    def test_navigate_from_products_to_product_details(self):
        self.login_page.do_login()
        self.products_page.select_first_item_to_see_detail()
        detail = self.product_detail_page.get_product_page_title()  
        self.assertTrue(detail.text == 'Back to products')

    def test_menu(self):
        self.login_page.do_login()
        menu = self.menu_wrap.menu()
        self.assertTrue(menu['all_items'].text == 'All Items')
        self.assertTrue(menu['logout'].text == 'Logout')
        self.assertTrue(menu['about'].text == 'About')
        self.assertTrue(menu['reset'].text == 'Reset App State')

    def test_logout(self):
        self.login_page.do_login()
        self.menu_wrap.click_logout()
        title = self.login_page.find_login_title()  
        self.assertTrue(title.text == 'Swag Labs')

    def test_about(self):
        self.login_page.do_login()
        self.menu_wrap.click_about()
        about = self.about_page.get_about_text()
        self.assertTrue(about.text == 'The Sauce Test Toolchain')

    def test_all_items(self):
        self.login_page.do_login()
        self.menu_wrap.click_all_items()
        items = self.products_page.get_product_page_title()
        self.assertTrue(items.text == 'Products')
        
    def test_reset_app_state(self):
        self.login_page.do_login()
        cart = self.general.add_product_to_cart()
        self.assertTrue(cart.text == "1")
        self.menu_wrap.click_reset_app_state()

    def test_twitter_button(self):
        self.login_page.do_login()     
        self.footer_page.navigate_to_twitter()
        title = self.footer_page.get_title()
        self.assertTrue("Sauce Labs (@saucelabs) / X" == title)

    def test_facebook_button(self):
        self.login_page.do_login()     
        self.footer_page.navigate_to_facebook()
        title = self.footer_page.get_title()
        self.assertTrue("Sauce Labs" in title and "Facebook" in title)

    def test_linkedin_button(self):
        self.login_page.do_login()     
        self.footer_page.navigate_to_linkedin()
        title = self.footer_page.get_title()
        self.assertTrue("LinkedIn" in title)

    def test_Add_And_Remove_Item(self):
        self.login_page.do_login()      
        cart = self.products_page.add_first_product_to_cart()
        self.assertTrue(cart.text == "1")
        cart = self.products_page.remove_first_product_from_cart()
        self.assertTrue(cart.text == '')


if __name__ == '__main__':
    unittest.main()
