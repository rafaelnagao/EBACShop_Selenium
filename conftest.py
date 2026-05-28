import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://lojaebac.ebaconline.art.br/#"


@pytest.fixture(scope="function")
def driver():
    options = Options()

    is_ci = os.getenv("CI", "false").lower() == "true"

    if is_ci:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def setup(request, driver):
    if request.cls is not None:
        request.cls.driver = driver
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = f"{item.name}.png"
            file_path = screenshots_dir / file_name
            driver.save_screenshot(str(file_path))