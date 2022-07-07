import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def open_page():
    url = "https://the-internet.herokuapp.com"
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(5)

    driver.get(url)
    driver.maximize_window()

    yield driver
    driver.quit()
