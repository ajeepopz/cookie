

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SauceDemoAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def print_cookies(self):
        cookies = self.driver.get_cookies()
        print("Cookies:")
        for cookie in cookies:
            print(cookie)

    def login(self, username, password):
        self.navigate_to_url("https://www.saucedemo.com/")
        username_input = self.wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        # Wait for login to complete and verify dashboard title
        self.wait.until(EC.title_contains("Swag Labs"))

    def logout(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()

        # Verify logout
        self.wait.until(EC.url_contains("https://www.saucedemo.com/"))

    def run(self):
        print("Before login:")
        self.print_cookies()

        self.login("standard_user", "secret_sauce")

        print("After login:")
        self.print_cookies()

        self.logout()

        print("After logout:")
        self.print_cookies()

        self.driver.quit()


automation = SauceDemoAutomation()
automation.run()