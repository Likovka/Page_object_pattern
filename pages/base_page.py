import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url=None, timeout=10):
        self.browser = browser
        self.url = url or getattr(self, "PAGE_URL", None)
        self.timeout = timeout

    def open(self):
        if not self.url:
            raise ValueError("URL must be specified right in constructor or as PAGE_URL attribute")
        self.browser.get(self.url)

    def go_to_login_page(self):
        WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(BasePageLocators.LOGIN_LINK)).click()

    def go_to_basket_page(self):
        WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(BasePageLocators.BASKET_BUTTON)).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout)
             .until(EC.presence_of_element_located((how, what))))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1,
                          [TimeoutException]).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_text_equal(self, locator1, locator2):
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator1))
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator2))

        text1 = self.browser.find_element(*locator1).text
        text2 = self.browser.find_element(*locator2).text
        return text1 == text2

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        return True
