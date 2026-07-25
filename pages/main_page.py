from .base_page import BasePage


class MainPage(BasePage):
    PAGE_URL = "http://selenium1py.pythonanywhere.com/"


    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
