from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductsDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_page_title(self):
        return self.driver.find_element(By.CLASS_NAME,'inventory_details_back_button')

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        time.sleep(5)
        return self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    
    def navegate_to_products_page(self):
        btn_return_to_products = self.driver.find_element(By.ID, "back-to-products")
        btn_return_to_products.click()
        return self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    
    def select_product_detail_menu(self):
        return self.driver.find_element(By.XPATH, f"//div[@class='bm-burger-button']/button")
    
    def menu(self):
        button = self.select_product_detail_menu()
        button.click()
        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        all_items_link = self.driver.find_element(By.ID, "inventory_sidebar_link")
        about_link = self.driver.find_element(By.ID, "about_sidebar_link")
        reset_link = self.driver.find_element(By.ID, "reset_sidebar_link")
        time.sleep(3)
        return {"all_items":all_items_link,"logout":logout_link,"about":about_link,"reset":reset_link}
    
    def logout(self):
        button = self.select_product_detail_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()

    def about(self):
        button = self.select_product_detail_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        about_link = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))
        about_link.click()