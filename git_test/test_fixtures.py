"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser, have
import pytest

desktop_windows_size = [(1920, 1080),
                        (1600, 900),
                        (1366, 768)]

mobile_windows_size = [(390, 844),
                       (412, 915),
                       (353, 745)]


@pytest.fixture(params=desktop_windows_size)
def desktop_windows_size(request):
    return request.param


def test_github_desktop(desktop_windows_size):
    browser.open('')
    browser.driver.set_window_size(desktop_windows_size[0] ,
                                   desktop_windows_size[1])
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.fixture(params=mobile_windows_size)
def all_windows_size(request):
    return request.param


def test_github_mobile(all_windows_size):
    browser.open('')
    browser.driver.set_window_size(all_windows_size[0],
                                   all_windows_size[1])
    browser.element(".Button[aria-label='Toggle navigation']").click()
    browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in'))
