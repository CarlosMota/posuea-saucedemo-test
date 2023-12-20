import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FooterPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_twitter(self):
        link = self.driver.find_element(By.XPATH,"//li[contains(@class,'social_twitter')]/a")
        link.click()
        time.sleep(3)

    def navigate_to_facebook(self):
        link = self.driver.find_element(By.XPATH,"//li[contains(@class,'social_facebook')]/a")
        link.click()
        time.sleep(3)

    def navigate_to_linkedin(self):
        link = self.driver.find_element(By.XPATH,"//li[contains(@class,'social_linkedin')]/a")
        link.click()
        time.sleep(3)

    def get_title(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[1])
        title = self.driver.title
        time.sleep(3)
        return title
    
    
