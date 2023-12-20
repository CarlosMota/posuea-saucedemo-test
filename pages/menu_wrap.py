from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MenuWrap:
    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        return self.driver.find_element(By.XPATH, f"//div[@class='bm-burger-button']/button")
    
    def menu(self):
        button = self.click_menu()
        button.click()
        logout_link = self.driver.find_element(By.ID, "logout_sidebar_link")
        all_items_link = self.driver.find_element(By.ID, "inventory_sidebar_link")
        about_link = self.driver.find_element(By.ID, "about_sidebar_link")
        reset_link = self.driver.find_element(By.ID, "reset_sidebar_link")
        time.sleep(3)
        return {"all_items":all_items_link,"logout":logout_link,"about":about_link,"reset":reset_link}
    
    def click_logout(self):
        button = self.click_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        time.sleep(3)
        
    def click_about(self):
        button = self.click_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        about_link = wait.until(EC.element_to_be_clickable((By.ID, "about_sidebar_link")))
        about_link.click()
        time.sleep(3)
        
    def click_all_items(self):
        button = self.click_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        all_itens_link = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
        all_itens_link.click()
        time.sleep(3)
    
    def click_reset_app_state(self):
        button = self.click_menu()
        button.click()
        wait = WebDriverWait(self.driver, 10)
        reset_app_state_link = wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link")))
        reset_app_state_link.click()
        time.sleep(3)