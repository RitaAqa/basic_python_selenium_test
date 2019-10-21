class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_button_allow(self):
        self.driver.find_element_by_xpath("//*[text() = 'Not Now']").clear()

