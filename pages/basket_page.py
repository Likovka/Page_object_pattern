from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/basket/"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be"

    def guest_can_see_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There are should be an empty basket message"