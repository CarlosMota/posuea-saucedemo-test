from selenium.webdriver.common.by import By

class CkeckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_checkout_button(self):
        return self.driver.find_element(By.CLASS_NAME,'checkout_button')