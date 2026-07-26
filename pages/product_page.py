from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

    def add_to_basket(self):
        WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)).click()

    def compare_names(self):
        assert self.is_text_equal(ProductPageLocators.PRODUCT_NAME,
                                  ProductPageLocators.PRODUCT_NAME_IN_BASKET), "Products names are not equal"

    def compare_prices(self):
        assert self.is_text_equal(ProductPageLocators.PRODUCT_PRICE,
                                  ProductPageLocators.PRODUCT_PRICE_IN_BASKET), "Products prices are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
