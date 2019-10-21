class SignInPage():

#
    def __init__(self, driver):
        self.driver = driver

    def create_account_button(self):
        self.driver.find_element_by_xpath("//*[text()='Створити обліковий запис']").click()

    def for_myself_button(self):
        self.driver.find_element_by_xpath("//*[text()='Для себе']").click()
