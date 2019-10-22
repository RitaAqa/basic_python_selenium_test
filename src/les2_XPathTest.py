## XPath Help https://devhints.io/xpath
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.instagram.com/")
login_field = driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")
login_field.click()
time.sleep(1)
login1_field = driver.find_element_by_xpath("//input[@name='username']")
login1_field.send_keys("ggg")


#dif Xpath for Google search field
#driver.get("https://www.google.com/")
#xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
#xpath("//div[@class='a4bIc']/input")
#xpath("//input[@class='gLFyf gsfi']")
#search_field = driver.find_element_by_xpath("//input[@name='q']")
#search_field.send_keys("ggg")
#driver.quit()
