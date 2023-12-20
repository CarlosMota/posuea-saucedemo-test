from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# products_page.py
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_page_title(self):
        return self.driver.find_element(By.CLASS_NAME,'title')

    def get_first_product_name(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'inventory_item_name')]").text
        

    def add_first_product_to_cart(self):
        
        product_name = self.get_first_product_name()
        
        add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        add_to_cart_button.click()

        return self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")

    def sort_products_to_az(self):

        select_element = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        
        select_element.click()
        option = self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']//option[@value='az']")
        
        option.click()

        return self.get_first_product_name()
    
    def sort_products_to_za(self):

        select_element = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        
        select_element.click()
        option = self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']//option[@value='za']")
        
        option.click()

        return self.get_first_product_name()

    def sort_products_to_low_to_high(self):

        select_element = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        
        select_element.click()
        option = self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']//option[@value='lohi']")
        
        option.click()

        return self.get_first_product_name()
    
    def sort_products_to_high_to_low(self):

        select_element = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        
        select_element.click()
        option = self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']//option[@value='hilo']")
        
        option.click()

        return self.get_first_product_name()
        
    def select_first_item_to_see_detail(self):

        product_name = self.get_first_product_name()

        img = self.driver.find_element(By.XPATH, f"//img[@alt='{product_name}']")

        img.click()

    def select_product_menu(self):
        return self.driver.find_element(By.XPATH, f"//div[@class='bm-burger-button']/button")

    def menu(self):

        button = self.select_product_menu()

        button.click()

        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        all_items_link = self.driver.find_element(By.ID, "inventory_sidebar_link")
        about_link = self.driver.find_element(By.ID, "about_sidebar_link")
        reset_link = self.driver.find_element(By.ID, "reset_sidebar_link")

        time.sleep(3)

        return {"all_items":all_items_link,"logout":logout_link,"about":about_link,"reset":reset_link}

        
    def logout(self):

        button = self.select_product_menu()

        button.click()

        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))

        logout_link.click()

    def about(self):

        button = self.select_product_menu()

        button.click()

        wait = WebDriverWait(self.driver, 10)
        about_link = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))

        about_link.click()

    
