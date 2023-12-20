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

    def navigate_to_facebook(self):
        link = self.driver.find_element(By.XPATH,"//li[contains(@class,'social_facebook')]/a")
        link.click()

    def navigate_to_linkedin(self):
        link = self.driver.find_element(By.XPATH,"//li[contains(@class,'social_linkedin')]/a")
        link.click()

    def get_twitter_link(self):
        time.sleep(3)

        print('Preparar pra abrir a aba do twitter')

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        print('aguarda a abertura da outra aba')
        
        all_handles = self.driver.window_handles

        print('alterna a aba')

        self.driver.switch_to.window(all_handles[1])

        print('procurar titulo')

        title = self.driver.title
        
        return title
