# check if broken images is existing on page

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import requests


url = 'https://the-internet.herokuapp.com/'


def check_for_broken_image():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(6)

    driver.get(url)

    try:
        driver.find_element_by_link_text('Broken Images').click()
        image_list = driver.find_elements(By.TAG_NAME, "img")
        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
    finally:
        driver.quit()
        print('test over')


check_for_broken_image()
