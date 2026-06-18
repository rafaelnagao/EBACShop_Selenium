from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title
    
    def roll_down(self, times=1):
        action = ActionChains(self.driver)
        for _ in range(times):
            action.send_keys(Keys.PAGE_DOWN)
        action.perform()