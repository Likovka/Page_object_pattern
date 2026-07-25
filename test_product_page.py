import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["offer0",
                                   "offer1",
                                   "offer2",
                                   "offer3",
                                   "offer4",
                                   "offer5",
                                   "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail),
                                   "offer8",
                                   "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.solve_quiz_and_get_code()
    assert product_page.compare_names(), "Products names are not equal"
    assert product_page.compare_prices(), "Products prices are not equal"


TODO: "Нужны более осмысленные и детальные комментарии для ассертов"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.guest_can_see_empty_basket_message()
