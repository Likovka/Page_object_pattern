import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


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

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BUCKET_BUTTON).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Нельзя смешивать неявные и явные ожидания, но курс сказал, что надо.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout)
             .until(EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_text_equal(self, locator1, locator2):
        text1 = self.browser.find_element(*locator1).text
        text2 = self.browser.find_element(*locator2).text
        return text1 == text2

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        return True
