from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6>.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info div:last-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
