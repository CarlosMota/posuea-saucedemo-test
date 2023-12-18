from selenium.webdriver.common.by import By


class ProductsDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_page_title(self):
        return self.driver.find_element(By.CLASS_NAME,'inventory_details_back_button')
