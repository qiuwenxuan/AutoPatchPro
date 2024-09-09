from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'loginButton')
