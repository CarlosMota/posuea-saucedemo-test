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


class TestProductsPage(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_detail_page = ProductsDetailPage(self.driver)

    def tearDown(self):
        print("product page tear down")
        self.driver.quit()

    
    # def test_add_product_to_cart(self):
        
    #     self.login_page.do_login()

    #     cart = self.products_page.add_first_product_to_cart()

    #     self.assertTrue(cart.text == "1")

    # def test_sort_product_to_az(self):

    #     self.login_page.do_login()

    #     first_product = self.products_page.sort_products_to_az()

    #     self.assertTrue(first_product == "Sauce Labs Backpack")

    # def test_sort_product_to_za(self):

    #     self.login_page.do_login()

    #     first_product = self.products_page.sort_products_to_za()

    #     self.assertTrue(first_product == "Test.allTheThings() T-Shirt (Red)")


    # def test_sort_product_to_low_to_high(self):

    #     self.login_page.do_login()

    #     first_product = self.products_page.sort_products_to_low_to_high()

    #     self.assertTrue(first_product == "Sauce Labs Onesie")

    # def test_sort_product_to_high_to_low(self):

    #     self.login_page.do_login()

    #     first_product = self.products_page.sort_products_to_high_to_low()

    #     self.assertTrue(first_product == "Sauce Labs Fleece Jacket")

    # def test_navigate_from_products_to_cart(self):

    #     self.login_page.do_login()

    #     cart = self.products_page.add_first_product_to_cart()

    #     cart.click()

    #     cart_button = self.cart_page.get_cart_title()

    #     self.assertTrue(cart_button.text == 'Your Cart')

    # def test_navigate_from_products_to_product_details(self):

    #     self.login_page.do_login()

    #     self.products_page.select_first_item_to_see_detail()

    #     detail = self.product_detail_page.get_product_page_title()
        
    #     self.assertTrue(detail.text == 'Back to products')

    def test_menu(self):
        self.login_page.do_login()

        menu = self.products_page.menu()

        self.assertTrue(menu['all_items'].text == 'All Items')
        self.assertTrue(menu['logout'].text == 'Logout')
        self.assertTrue(menu['about'].text == 'About')
        self.assertTrue(menu['reset'].text == 'Reset App State')

    def test_logout(self):

        self.login_page.do_login()

        self.products_page.logout()

        title = self.login_page.find_login_title()

        print("titulo do login encontrado")

        self.assertTrue(title.text == 'Swag Labs')            

if __name__ == '__main__':
    unittest.main()
