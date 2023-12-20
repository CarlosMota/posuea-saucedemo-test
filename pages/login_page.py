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
        time.sleep(3)
        
        
    def load_credentials(self):
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        credentials = config_data.get("login_credentials", {})
        print(credentials["username"])
        time.sleep(3)
        return {"username":credentials["username"], "password":credentials["password"]}
    
    def do_login(self):
        credentials = self.load_credentials()
        self.login(username=credentials["username"],password=credentials["password"])
        time.sleep(3)

    
    def find_error_message(self):
        time.sleep(3)
        return self.driver.find_element(By.XPATH,'//div[@class="error-message-container error"]/h3')
    
    def find_login_title(self):
        print("Encontrar titulo do login")
        time.sleep(3)
        return self.driver.find_element(By.XPATH,'//div[@class="login_logo"]')
    