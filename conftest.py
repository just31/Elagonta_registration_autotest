import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():

    # driver = webdriver.Chrome()
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities={
            "browserName": "firefox",
            "video": "True",
            "platform": "WIN10",
            "platformName": "windows",
            'javascriptEnabled': True
        })
    # Открываем браузер во весь экран.
    driver.maximize_window()
    # Используем конструкцию yield, которая разделяет функцию browser() на часть — до тестов и после тестов.
    yield driver
    driver.quit()
