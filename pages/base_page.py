from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        url_to_open = None
        if self.url:
            url_to_open = self.url
        elif hasattr(self, "PAGE_URL"):
            url_to_open = self.PAGE_URL
        else:
            raise ValueError("There should be URL")
        self.browser.get(url_to_open)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
