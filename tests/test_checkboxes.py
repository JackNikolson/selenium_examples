import time

def test_checkboxes(open_page):
    driver = open_page
    driver.find_element_by_css_selector('#content > ul > li:nth-child(6) > a').click()
    assert driver.find_element_by_xpath('//*[@id="content"]/div/h3'), 'Checkbox title not presented on page'


    checkboxes = driver.find_elements_by_css_selector('#checkboxes')    
    
    for checkbox in checkboxes:
        if checkbox.is_selected() == False:
            driver.execute_script("document.getElementById('checkboxes').click()")
        assert checkbox.is_selected()
