from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = get_logger(__name__)

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.logo = (By.CSS_SELECTOR, "img.logo-img")
        self.search_icon = (By.CSS_SELECTOR, 'button[data-target^="#searchformshow-"]')
        self.cart_link = (By.CSS_SELECTOR, "a.dropdown-toggle.mini-cart")
        self.navigation_menu = (By.CSS_SELECTOR, "#primary-menu")
        self.products_section = (By.CSS_SELECTOR, "#main > div.vc_row.wpb_row.vc_row-fluid.vc_custom_1503474667302 > div")
        self.footer = (By.CSS_SELECTOR, "#tbay-footer > div > div > div > div")
        self.sidebar = (By.CSS_SELECTOR, "#wrapper-container > div.tbay-to-top.v4.active")

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
    
    def is_navigation_menu_displayed(self):
        return self._has_visible_element(self.navigation_menu)

    def is_products_section_displayed(self):
        return self._has_visible_element(self.products_section)

    def is_footer_displayed(self):
        return self._has_visible_element(self.footer)

    def is_sidebar_displayed(self):
        BasePage(self.driver).roll_down(times=3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sidebar))
        return self._has_visible_element(self.sidebar)