from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_title(self):
        time.sleep(3)
        return self.driver.find_element(By.CLASS_NAME,'title')
    
    def navegate_to_products_page(self):
        btn_navegate_to_products = self.driver.find_element(By.ID, "continue-shopping")
        btn_navegate_to_products.click()
        time.sleep(3)
        return self.driver.find_element(By.ID, "inventory_container")
    
    def navegate_to_checkout_page(self):
        btn_navegate_to_products = self.driver.find_element(By.ID, "checkout")
        btn_navegate_to_products.click()
        time.sleep(3)
        return self.driver.find_element(By.ID, "checkout_info_container")