import pytest
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
@pytest.mark.home
@pytest.mark.e2e
class TestHomeMenuBar:
    def test_mouse_hover_menu(self):
        home_page = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.menu_home)).click()
        assert home_page.is_submenu_home_dropdown_displayed()

    def test_click_menu_item(self):
        home_page = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.menu_home)).click()
        assert home_page.get_current_url() == "http://lojaebac.ebaconline.art.br/home/"
        assert home_page.get_current_title() == "Home – EBAC – Shop"
    
    def test_click_submenu_item(self):
        home_page = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.menu_home)).click()
        home_page.click_submenu_item(home_page.submenu_home_dropdown_item10)
        assert home_page.get_current_url() == "http://lojaebac.ebaconline.art.br/home-10/"
        assert home_page.get_current_title() == "Home 10 – EBAC – Shop"
    
    def test_click_menu_comprar(self):
        home_page = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.menu_comprar)).click()
        assert home_page.get_current_url() == "http://lojaebac.ebaconline.art.br/produtos/"
        assert home_page.get_current_title() == "Produtos – EBAC – Shop"
    
    def test_click_submenu_blog(self):
        home_page = HomePage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.menu_blog)).click()
        home_page.click_submenu_item(home_page.submenu_blog_list)
        assert home_page.get_current_url() == "http://lojaebac.ebaconline.art.br/blog-lists/"
        assert home_page.get_current_title() == "Blog Lists – EBAC – Shop"
    
