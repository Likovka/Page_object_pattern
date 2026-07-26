import random
import string
import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def generate_register_data(type_data):
    match type_data:
        case "email":
            return str(time.time()) + "@fakemail.org"
        case "password":
            return "".join(random.choices(string.ascii_letters + string.digits, k=9))
        case _:
            return None


@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["offer0",
                                   "offer1",
                                   "offer2",
                                   "offer3",
                                   "offer4",
                                   "offer5",
                                   "offer6",
                                   pytest.param("offer7",
                                                marks=pytest.mark.xfail(reason="has wrong book name")),
                                   "offer8",
                                   "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.compare_names()
    product_page.compare_prices()


@pytest.mark.xfail(reason="Success message always shows after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message does not know how to disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.guest_can_see_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        page = LoginPage(self.browser)
        page.open()

        email = generate_register_data("email")
        password = generate_register_data("password")
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        product_page = ProductPage(self.browser)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        product_page = ProductPage(self.browser)
        product_page.open()
        product_page.add_to_basket()
        product_page.compare_names()
        product_page.compare_prices()
