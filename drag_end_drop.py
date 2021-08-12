from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
import time

url = "https://the-internet.herokuapp.com/drag_and_drop"


def drag_drop(url):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(6)

    driver.get(url)
    driver.maximize_window()

    box_a = driver.find_element_by_css_selector('#column-a')
    box_b = driver.find_element_by_css_selector('#column-b')

    action = ActionChains(driver)
    action.click_and_hold(box_a).pause(4).move_to_element(box_b).release(box_b).perform()

    driver.quit()
    print('test finished')

drag_drop(url)
