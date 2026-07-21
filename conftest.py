import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


@pytest.fixture(scope="function")
def browser(request):
    options = None
    browser = None

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Chrome_Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = Firefox_Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ")
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome or firefox")
