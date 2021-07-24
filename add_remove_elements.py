from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

url = "https://the-internet.herokuapp.com/"


def add_delete_button(url):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(6)

    driver.get(url)

    # search for link with Add/Remove Elements
    driver.find_element_by_xpath('//div[@id="content"]/ul/li[2]/a').click()
    time.sleep(3)

    add_button = driver.find_element_by_css_selector('#content > div > button')

    assert add_button
    print("Add buton is presented on page")
    add_button.click()

    # search for delete button
    del_button = driver.find_element_by_css_selector('#elements > button')
    assert del_button
    print("Delete button is presented on page")
    del_button.click()

    driver.quit()
    print("Test succeed")


add_delete_button(url)
