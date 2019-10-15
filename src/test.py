from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")
search_field.send_keys("JavaScript")
search_button.click()
assert "JavaScript" in driver.title

driver.quit()

