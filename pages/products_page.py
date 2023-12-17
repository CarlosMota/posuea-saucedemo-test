from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# products_page.py
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_title = driver.find_element(By.CLASS_NAME,'title')
