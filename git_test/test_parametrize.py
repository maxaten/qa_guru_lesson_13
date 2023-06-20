"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture()
def browser_size(request):
    resolutions = {
        'desktop': (1920, 1080),
        'mobile': (390, 844)
    }
    return resolutions[request.param]


@pytest.mark.parametrize('browser_size', ['desktop'], indirect=True)
def test_github_desktop(browser_size):
    browser.open('')
    browser.driver.set_window_size(*browser_size)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize('browser_size', ['mobile'], indirect=True)
def test_github_mobile(browser_size):
    browser.open('')
    browser.driver.set_window_size(*browser_size)
    browser.element(".Button[aria-label='Toggle navigation']").click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in'))