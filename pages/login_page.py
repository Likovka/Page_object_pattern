from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("/login/"), "This is not a login page"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        assert self.browser.find_element(*LoginPageLocators.SUCCESS_MESSAGE).text
