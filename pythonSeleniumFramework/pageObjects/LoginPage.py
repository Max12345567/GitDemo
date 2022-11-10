# we will store only the elements inside pageObjects and simply return that function


from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username0")
    password = (By.ID, "password1")
    remember_userid = (By.XPATH, "//label[@for='rememberuserid']")
    accept_login = (By.ID, "accept")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_remember_userid(self):
        return self.driver.find_element(*LoginPage.remember_userid)

    def get_accept_login(self):
        return self.driver.find_element(*LoginPage.accept_login)
