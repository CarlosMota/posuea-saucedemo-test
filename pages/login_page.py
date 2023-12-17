import os
import time
import json
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID,'user-name')
        self.password_input = driver.find_element(By.ID,'password')
        self.login_button = driver.find_element(By.ID,'login-button')

    def login(self,username,password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
        
        
    def load_credentials(self):
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        credentials = config_data.get("login_credentials", {})
        print(credentials["username"])
        return {"username":credentials["username"], "password":credentials["password"]}
    
    def find_error_message(self):
        return self.driver.find_element(By.XPATH,'//div[@class="error-message-container error"]/h3')
    