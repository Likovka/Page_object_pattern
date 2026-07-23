from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def compare_names(self):
        return self.is_text_equal(ProductPageLocators.PRODUCT_NAME, ProductPageLocators.PRODUCT_NAME_IN_BASKET)

    def compare_prices(self):
        return self.is_text_equal(ProductPageLocators.PRODUCT_PRICE, ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
