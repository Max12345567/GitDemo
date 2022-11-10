from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass): # this is inheritance
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        login.get_remember_userid().click()
        login.get_accept_login().click()

        trade = TradePage(self.driver)
        trade.get_symbol().click()
        trade.get_symbol().send_keys("TSLA")
        trade.get_symbol_lookup().click()
        trade.get_side().click()
        trade.get_quantity().click()
        trade.get_quantity_input()

        trade.get_review_order().click()
        trade.send_order().click()
        trade.
        #trade.get_order_confirmation().text("")
        assert trade.get_order_confirmation() == trade.get_order_confirmation().t



        self.driver.find_element(By.CSS_SELECTOR, "button[direction='buy']").click()

        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "li[data-testid='tif-dropdown:EXT']").click()
        sleep(2)

        sleep(4)
        print(self.driver.find_element(By.CSS_SELECTOR, "div[class='NotificationCardstyled__Text-liTWMR fhanmg']").
              get_attribute('innerHTML'))
        sleep(2)
        self.driver.close()
