from selenium import webdriver
import time

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://accounts.google.com")

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

time.sleep(1)
for_myself_button = driver.find_element_by_xpath("//*[text()='Для себя']")
for_myself_button.click()

#variables
validationError = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
user_dictionary = {'fn':'Alex', 'ln':'Kardash', 'password': 'Abc123456!'}


first_name_field.send_keys(user_dictionary['fn'])
last_name_field.send_keys(user_dictionary['ln'])
password_field.send_keys(user_dictionary['password'])
confirm_password_field.send_keys(user_dictionary["password"])


def validate_email_field(email):
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    time.sleep(1)
    assert validationError in driver.page_source

for email in email_list:
    validate_email_field(email)

driver.quit()




