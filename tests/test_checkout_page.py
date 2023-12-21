import unittest
from selenium.webdriver import Chrome

from pages.checkout_page import CheckoutPage
from pages.about_page import AboutPage
from pages.cart_page import CartPage
from pages.footer_page import FooterPage
from pages.general import General
from pages.login_page import LoginPage
from pages.menu_wrap import MenuWrap
from pages.products_detail_page import ProductsDetailPage
from pages.products_page import ProductsPage

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
        self.driver.get("https://www.saucedemo.com/")  
        self.login_page = LoginPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.about_page = AboutPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.footer_page = FooterPage(self.driver)
        self.general = General(self.driver)
        self.menu_wrap = MenuWrap(self.driver)
        self.product_detail_page = ProductsDetailPage(self.driver)
        self.products_page = ProductsPage(self.driver)

    def tearDown(self):
        print("checkout page tear down")
        self.driver.quit()

    def test_complete_checkout_process(self):
        self.login_page.do_login()
        self.products_page.add_first_product_to_cart()
        self.products_page.go_to_checkout()

        self.checkout_page.proceed_to_checkout()
        self.assertIn("checkout-step-one", self.driver.current_url)
        checkout_title = self.checkout_page.get_checkout_page_title()
        self.assertEqual(checkout_title.text, 'Checkout: Your Information')

        self.checkout_page.fill_checkout_form("John", "Doe", "123456")
        self.checkout_page.continue_checkout()
        self.assertIn("checkout-step-two", self.driver.current_url)

        self.checkout_page.click_finish_button()
        self.assertIn("checkout-complete", self.driver.current_url)
        checkout_complete_title = self.checkout_page.get_checkout_complete_title()
        self.assertEqual(checkout_complete_title.text, 'Checkout: Complete!')

        self.checkout_page.click_return_home_button()
        self.assertIn("inventory", self.driver.current_url)
        title = self.products_page.get_product_page_title()
        self.assertIn("Products", title.text)

    def test_cancel_checkout(self):
        self.login_page.do_login()
        self.products_page.add_first_product_to_cart()
        self.products_page.go_to_checkout()

        self.checkout_page.proceed_to_checkout()
        self.assertIn("checkout-step-one", self.driver.current_url)
        checkout_title = self.checkout_page.get_checkout_page_title()
        self.assertEqual(checkout_title.text, 'Checkout: Your Information')

        self.checkout_page.click_back_cart_button()
        self.assertIn("cart", self.driver.current_url)
    
    def test_cancel_detail_checkout(self):
        self.login_page.do_login()
        self.products_page.add_first_product_to_cart()
        self.products_page.go_to_checkout()
        
        self.checkout_page.proceed_to_checkout()
        self.assertIn("checkout-step-one", self.driver.current_url)
        checkout_title = self.checkout_page.get_checkout_page_title()
        self.assertEqual(checkout_title.text, 'Checkout: Your Information')

        self.checkout_page.fill_checkout_form("John", "Doe", "123456")
        self.checkout_page.continue_checkout()
        self.assertIn("checkout-step-two", self.driver.current_url)
        checkout_title = self.checkout_page.get_checkout_detail_title()
        self.assertEqual(checkout_title.text, 'Checkout: Overview')
        
        self.checkout_page.click_cancel_checkout_button()
        self.assertIn("inventory", self.driver.current_url)
        title = self.products_page.get_product_page_title()
        self.assertIn("Products", title.text)

    def test_valid_form(self):
        self.login_page.do_login()
        self.products_page.add_first_product_to_cart()
        self.products_page.go_to_checkout()

        self.checkout_page.proceed_to_checkout()
        self.assertIn("checkout-step-one", self.driver.current_url)
        checkout_title = self.checkout_page.get_checkout_page_title()
        self.assertEqual(checkout_title.text, 'Checkout: Your Information')

        self.checkout_page.fill_checkout_form("John", "Doe", "")
        self.checkout_page.continue_checkout()
        message_return = self.checkout_page.get_message_error()
        self.assertEqual(message_return, "Error: Postal Code is required")
    
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

if __name__ == '__main__':
    unittest.main()