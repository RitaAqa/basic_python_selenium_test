class SignUp():

    validationError = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name_field(self, first_name_field):
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id("firstName").send_keys(first_name_field)

    def enter_last_name_field(self, last_name_field):
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id("lastName").send_keys(last_name_field)

    def enter_password(self, password):
        self.driver.find_element_by_name("Passwd").clear
        self.driver.find_element_by_name("Passwd").send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element_by_name("ConfirmPasswd").clear()
        self.driver.find_element_by_name("ConfirmPasswd").send_keys(confirm_password)

    def username_field(self, username_field):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username_field)

    def login(self):
        self.driver.find_element_by_id("accountDetailsNext").click()

