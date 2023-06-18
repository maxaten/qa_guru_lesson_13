import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.base_url = 'https://github.com'
    browser.open('/')

    yield

    browser.quit()
