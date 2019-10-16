from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

driver.get("https://www.instagram.com/")
login_field = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login_field.click()
login1_field = driver.find_element_by_xpath("//input[@name='username']")
login1_field.send_keys("ggg")


