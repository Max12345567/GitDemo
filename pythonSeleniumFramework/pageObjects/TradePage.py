# getters - what ever we have created are the getter because they get that respect elements.
# setters - since we get and set we send keys that would be setters.
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# * we need it to conver it into tuple
class TradePage:
    def __init__(self, driver):
        self.driver = driver

    trade_button = (By.XPATH, "//button[@data-testid='trade-page-button']")
    symbol = (By.ID, "navigation-symbol-search")
    symbol_lookup = (By.XPATH, "//*[@id='tippy-1']/div/div/div/div/div/ul/li[2]/div/div[1]/span/mark")
    side = (By.XPATH, "//buttom[@")
    quantity = (By.XPATH, "input[@type='number']")
    time_in_force = (By.XPATH, "//*[@id='tradeTicket-0']/div[2]/div[5]/button/div")

    review_order = (By.CSS_SELECTOR, )
    send_order = (By.CSS_SELECTOR, )
    notification = (By.XPATH, )
    original_message = (By.XPATH, )

    # self.driver.find_element(By.ID, "review-order-button").click()
    # sleep(2)
    # self.driver.find_element(By.ID, "send-order-button").click()

    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade_button)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_lookup(self):
        return self.driver.find_element(*TradePage.symbol_lookup)

    def get_side(self):
        return self.driver.find_element(*TradePage.side)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        quantity_input = self.driver.find_element(*TradePage.quantity)
        for i in range(3):
            quantity_input.send_keys(Keys.BACK_SPACE)
        quantity_input.send_keys(15)
        return quantity_input
    def get_time_in_force(self):
        return self.driver.find_element(*TradePage.time_in_force)

    def get_review_order(self):
        return self.driver.find_element(*TradePage.review_order)

    def get_send_order(self):
        return self.driver.find_element(*TradePage.send_order)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):
        original_confirmation = []
        original_message = [
            self.driver.find_element(*TradePage.original_message)]
