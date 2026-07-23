import pytest

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
