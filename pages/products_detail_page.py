from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductsDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_page_title(self):
        time.sleep(3)
        return self.driver.find_element(By.CLASS_NAME,'inventory_details_back_button')
    
    def navegate_to_products_page(self):
        btn_return_to_products = self.driver.find_element(By.ID, "back-to-products")
        btn_return_to_products.click()
        time.sleep(3)
        return self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    
    # def select_product_detail_menu(self):
    #     return self.driver.find_element(By.XPATH, f"//div[@class='bm-burger-button']/button")