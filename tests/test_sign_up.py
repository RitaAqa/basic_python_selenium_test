from selenium import webdriver
from sign_in_page import SignInPage
from create_account_page import SignUp
import time
#
validationError = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."
user_dictionary = {'fn': 'Alex', 'ln': 'Kardash', 'password': 'Abc123456!'}
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}


driver = webdriver.Chrome("C:/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://accounts.google.com")

sign_in_page = SignInPage(driver)
sign_in_page.create_account_button()
time.sleep(1)
sign_in_page.for_myself_button()


create_account_page = SignUp(driver)
create_account_page.enter_first_name_field(user_dictionary['fn'])
create_account_page.enter_last_name_field(user_dictionary['ln'])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.enter_confirm_password(user_dictionary["password"])


def validate_email_field(email):
    create_account_page.username_field(email)
    create_account_page.login()
    time.sleep(1)
    assert validationError in driver.page_source

for email in email_list:
    validate_email_field(email)

driver.quit()
