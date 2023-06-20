"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have

windows_size = [(1920, 1080),
                (1600, 900),
                (1366, 768),
                (390, 844),
                (412, 915),
                (353, 745)]


@pytest.fixture(params=windows_size)
def all_windows_size(request):
    return request.param


def test_github(all_windows_size):
    if all_windows_size[0] > 900:
        test_github_desktop(all_windows_size)
    if all_windows_size[1] < 900:
        test_github_mobile(all_windows_size)


def test_github_desktop(all_windows_size):
    browser.open('')
    browser.driver.set_window_size(all_windows_size[0],
                                   all_windows_size[1])
    if all_windows_size[0] < 900:
        pytest.skip(reason='Некорректное разрешение экрана')
    else:
        browser.element('.HeaderMenu-link--sign-in').click()
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(all_windows_size):
    browser.open('')
    browser.driver.set_window_size(all_windows_size[0],
                                   all_windows_size[1])
    if all_windows_size[0] > 900:
        pytest.skip(reason='Некорректное разрешение экрана')
    else:
        browser.element(".Button[aria-label='Toggle navigation']").click()
        browser.element('.HeaderMenu-link--sign-in').should(have.text('Sign in'))