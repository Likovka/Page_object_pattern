from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def compare_names(self):
        return self.is_text_equal(ProductPageLocators.PRODUCT_NAME, ProductPageLocators.PRODUCT_NAME_IN_BASKET)

    def compare_prices(self):
        return self.is_text_equal(ProductPageLocators.PRODUCT_PRICE, ProductPageLocators.PRODUCT_PRICE_IN_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
