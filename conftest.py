import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    # Открываем браузер во весь экран.
    driver.maximize_window()
    # Используем конструкцию yield, которая разделяет функцию browser() на часть — до тестов и после тестов.
    yield driver
    driver.quit()
