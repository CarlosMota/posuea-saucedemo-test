import os
import time
import json
from selenium.webdriver.common.by import By

class General:
    def __init__(self,driver):
        self.driver = driver
        
    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        time.sleep(3)
        return self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    
    def remove_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        add_to_cart_button.click()
        time.sleep(3)
        return True
        ##self.driver.find_element(By.ID, "cart_contents_container")
    
    def get_value_cart(self):
        time.sleep(3)
        return self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_link']")
    
    def navegate_to_cart_page(self):
        btn_navegate_to_products = self.driver.find_element(By.ID, "shopping_cart_container")
        btn_navegate_to_products.click()
        time.sleep(3)
        return btn_navegate_to_products
    
    def navegate_to_product_detail_page(self):
        btn_navegate_to_products = self.driver.find_element(By.ID, "item_4_title_link")
        btn_navegate_to_products.click()
        time.sleep(3)
        return btn_navegate_to_products