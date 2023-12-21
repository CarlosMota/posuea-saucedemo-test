from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_checkout_page_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'title')
    
    def get_checkout_complete_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'title')
    
    def get_checkout_detail_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'title')
    
    def proceed_to_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        checkout_button.click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        firstname_input = self.driver.find_element(By.ID, 'first-name')
        #firstname_input.send_keys(first_name)
        lastname_input = self.driver.find_element(By.ID, 'last-name')
        #lastname_input.send_keys(last_name)
        postalcode_input = self.driver.find_element(By.ID, 'postal-code')
        #postalcode_input.send_keys(postal_code)
    
        # Verificar se os campos estão vazios antes de preenchê-los
        #if not first_name:
        #    raise ValueError("O campo 'first_name' não pode estar vazio.")
        #if not last_name:
        #    raise ValueError("O campo 'last_name' não pode estar vazio.")
        #if not postal_code:
        #    raise ValueError("O campo 'postal_code' não pode estar vazio.")

        firstname_input.clear()
        firstname_input.send_keys(first_name)

        lastname_input.clear()
        lastname_input.send_keys(last_name)

        postalcode_input.clear()
        postalcode_input.send_keys(postal_code)
    
    #time.sleep(3)
    
    def continue_checkout(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'continue'))
        )
        continue_button.click()
    
    def click_back_cart_button(self):
        cancel_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'cancel'))
        )
        cancel_button.click()
    
    #time.sleep(3)
    
    def click_finish_button(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'finish'))
        )
        finish_button.click()
    
    #time.sleep(4)

    def click_return_home_button(self):
        return_home_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'back-to-products'))
        )
        return_home_button.click()
    
    #time.sleep(4)

    def get_message_error(self):
        message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        return message.text

    def click_cancel_checkout_button(self):
        return_home_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'cancel'))
        )
        return_home_button.click()