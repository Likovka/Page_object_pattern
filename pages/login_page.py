from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/"in self.browser.current_url, f"Expecting '/login/' in URL but got '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)

        password_repeat = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        password_repeat.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

        assert self.browser.find_element(*LoginPageLocators.SUCCESS_MESSAGE).text
