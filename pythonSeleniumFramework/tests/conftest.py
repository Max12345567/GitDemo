from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from testLoginData.TestLoginData import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver  # it doesn't matter where your driver is it will be applied anywhere within out method
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\makhm\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.get("http://shopping.beeyor.com/")
    elif browser_name == "firefox":
        service_obj = Service("C:\\Users\\makhm\\AppData\\Local\\Programs\\Python\\Python310\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.get("https://trade.thinkorswim.com/")
    driver.implicitly_wait(15)
    driver.minimize_window()
    driver.maximize_window()
    request.cls.driver = driver
    yield  # teardown method
    # return driver
    driver.close()

    # request is an instance, and we can set it in def, and we can use it in 14 and 20, it will form a connection

    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param
