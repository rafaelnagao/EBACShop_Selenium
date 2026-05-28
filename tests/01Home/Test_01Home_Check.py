import pytest
from pages.home_page import HomePage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.usefixtures("setup")
@pytest.mark.home
@pytest.mark.e2e
class Test_HomeCheck:
    def test_home_title(self):
        home_page = HomePage(self.driver)
        title = home_page.get_home_title()
        logger.info(f"Home page title: {title}")
        assert title == "EBAC – Shop – Página de teste"
    
    def test_home_url(self):
        home_page = HomePage(self.driver)
        url = home_page.get_home_url()
        logger.info(f"Home page URL: {url}")
        assert url == "http://lojaebac.ebaconline.art.br/#"

    def test_logo_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_logo_displayed(), "Logo should be displayed on the home page"
    
    def test_search_icon_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_search_icon_displayed(), "Search icon should be displayed on the home page"

    def test_cart_link_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_cart_link_displayed(), "Cart link should be displayed on the home page"