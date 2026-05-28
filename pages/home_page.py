from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.logo = (By.CSS_SELECTOR, "img.logo-img")
        self.search_icon = (By.CSS_SELECTOR, 'button[data-target^="#searchformshow-"]')
        self.cart_link = (By.CSS_SELECTOR, "a.dropdown-toggle.mini-cart")

    def get_home_title(self):
        return self.driver.title

    def get_home_url(self):
        return self.driver.current_url

    def _has_visible_element(self, locator):
        elements = self.driver.find_elements(*locator)
        visible = [el for el in elements if el.is_displayed()]
        logger.info(f"{locator} -> found={len(elements)}, visible={len(visible)}")
        return len(visible) > 0

    def is_logo_displayed(self):
        return self._has_visible_element(self.logo)

    def is_search_icon_displayed(self):
        return self._has_visible_element(self.search_icon)

    def is_cart_link_displayed(self):
        return self._has_visible_element(self.cart_link)