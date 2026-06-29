from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

logger = get_logger(__name__)

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.logo = (By.CSS_SELECTOR, "img.logo-img")
        self.search_icon = (By.CSS_SELECTOR, "div.search-form > button[data-toggle='modal']")
        self.cart_link = (By.CSS_SELECTOR, "a.dropdown-toggle.mini-cart")
        self.navigation_menu = (By.CSS_SELECTOR, "#primary-menu")
        self.products_section = (By.CSS_SELECTOR, "#main > div.vc_row.wpb_row.vc_row-fluid.vc_custom_1503474667302 > div")
        self.footer = (By.CSS_SELECTOR, "#tbay-footer > div > div > div > div")
        self.sidebar = (By.CSS_SELECTOR, "#wrapper-container > div.tbay-to-top.v4.active")
        self.submenu = (By.CSS_SELECTOR, "#primary-menu > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-has-children.menu-item-29 > ul")
        self.menu_home = (By.CSS_SELECTOR, "#primary-menu > li.dropdown.active.menu-item-536.aligned-left > a")
        self.submenu_home_dropdown = (By.CSS_SELECTOR, "#primary-menu > li.dropdown.active.menu-item-536.aligned-left > ul")
        self.submenu_home_dropdown_item10 = (By.CSS_SELECTOR, "#primary-menu > li.dropdown.active.menu-item-536.aligned-left > ul > li.menu-item-977.aligned-")
        self.menu_comprar = (By.CSS_SELECTOR, "#primary-menu > li.menu-item-629.aligned-fullwidth")
        self.menu_blog = (By.CSS_SELECTOR, "#primary-menu > li.dropdown.menu-item-196.aligned-left")
        self.submenu_blog_list = (By.CSS_SELECTOR, "#primary-menu > li.dropdown.menu-item-196.aligned-left > ul > li.menu-item-198.aligned-")
        self.search_modal = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div")
        self.search_dropdown = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div > div.modal-body > div > form > div > div > div.select-category.input-group-addon > div")
        self.search_dropdown_item = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div > div.modal-body > div > form > div > div > div.select-category.input-group-addon > div > div > ul > li:nth-child(3)")
        self.search_dropdown_item_selected = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div > div.modal-body > div > form > div > div > div.select-category.input-group-addon > div > p")
        self.search_input = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div > div.modal-body > div > form > div > div > input.tbay-search.form-control.input-sm.ui-autocomplete-input")
        self.search_wrapper = (By.CSS_SELECTOR, "[id^='searchformshow-'] > div > div > div.modal-body >	div > form >	div >	div >	div.tbay-search-result-wrapper")

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
    
    def get_menu_element(self):
        return self.driver.find_element(*self.navigation_menu)
    
    def mouse_hover(self, locator):
        ActionChains(self.driver)\
            .move_to_element(self.driver.find_element(*locator))\
            .perform()
    
    def click_menu_item(self, locator):
        menu_item_element = self.driver.find_element(*locator)
        menu_item_element.click()

    def click_submenu_item(self, locator):
        submenu_item_element = self.driver.find_element(*locator)
        submenu_item_element.click()

    def is_submenu_home_dropdown_displayed(self):
        return self._has_visible_element(self.submenu_home_dropdown)
    
    def get_current_url(self):
        return self.driver.current_url

    def get_current_title(self):
        return self.driver.title
    
    def is_search_modal_displayed(self):
        return self._has_visible_element(self.search_modal)

    def click_search_dropdown(self):
        search_dropdown_element = self.driver.find_element(*self.search_dropdown)
        search_dropdown_element.click()

    def click_search_dropdown_item(self):
        search_dropdown_item_element = self.driver.find_element(*self.search_dropdown_item)
        search_dropdown_item_element.click()
    
    def get_selected_dropdown_text(self):
        return self.driver.find_element(*self.search_dropdown_item_selected).text
    
    def is_search_wrapper_displayed(self):
        return self._has_visible_element(self.search_wrapper)