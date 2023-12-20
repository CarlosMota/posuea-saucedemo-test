import os
import time
import json
from selenium.webdriver.common.by import By


class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_about_text(self):
        time.sleep(3)
        return self.driver.find_element(By.CLASS_NAME,'css-1nxptes')
