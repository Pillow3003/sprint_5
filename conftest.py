import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options = options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def url(driver):
    driver.get(data.Urls.url)
    yield driver



