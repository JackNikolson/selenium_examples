import pytest
import time


@pytest.mark.auth
def test_open_auth_page(open_page):
    driver = open_page

    try:
        driver.find_element_by_link_text('Form Authentication').click()

        login_field = driver.find_element_by_xpath('//*[@id="username"]')
        password_field = driver.find_element_by_xpath('//*[@id="password"]')
        login_btn = driver.find_element_by_xpath('//*[@id="login"]/button/i')
        assert login_field.is_displayed()
        assert password_field.is_displayed()
        assert login_btn.is_displayed()

        login_field.send_keys('tomsmith')
        password_field.send_keys('SuperSecretPassword!')
        login_btn.click()

        time.sleep(3)
    finally:
        driver.quit()
