import pytest
from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.usefixtures("setup")
@pytest.mark.home
@pytest.mark.e2e
class TestHomeCheck:
    def test_title(self):
        home_page = HomePage(self.driver)
        title = home_page.get_home_title()
        logger.info(f"Home page title: {title}")
        assert title == "EBAC – Shop – Página de teste"
    
    def test_url(self):
        home_page = HomePage(self.driver)
        url = home_page.get_home_url()
        logger.info(f"Home page URL: {url}")
        assert url == "http://lojaebac.ebaconline.art.br/#"

    def test_logo_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_logo_displayed()
    
    def test_search_icon_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_search_icon_displayed()

    def test_cart_link_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_cart_link_displayed()

    def test_navigation_menu_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_navigation_menu_displayed()

    def test_products_section_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_products_section_displayed()

    def test_footer_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_footer_displayed()

    def test_sidebar_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_sidebar_displayed()