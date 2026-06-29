import pytest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
@pytest.mark.home
@pytest.mark.e2e
class TestHomeSearch:
    def test_search_modal_displayed(self):
        home_page = HomePage(self.driver)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.search_icon)).click()        
        assert home_page.is_search_modal_displayed()

    def test_search_dropdown(self):
        home_page = HomePage(self.driver)
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.search_icon)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(home_page.search_modal))
        
        home_page.click_search_dropdown()
        home_page.click_search_dropdown_item()

        assert home_page.get_selected_dropdown_text() == "Men"
    
    def test_search_input(self):
        home_page = HomePage(self.driver)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.search_icon)).click()
        
        search_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.search_input))
        search_input.click()
        search_input.send_keys("rou")
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.search_wrapper))
        assert search_input.get_attribute("value") == "rou"
        assert home_page.is_search_wrapper_displayed()