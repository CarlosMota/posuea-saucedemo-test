from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# products_page.py
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_title = driver.find_element(By.CLASS_NAME,'title')

    def add_first_product_to_cart(self):
        
        product_name = self.driver.find_element(By.XPATH, "//div[contains(@class,'inventory_item_name')]").text
        
        add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        add_to_cart_button.click()

        time.sleep(3)

        return self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")

