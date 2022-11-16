from src.components.cart import Cart
from src.pages.base_page import BasePage
from playwright.sync_api import TimeoutError
from allure import step


class ShopPage(BasePage):
    _PRODUCT_BUTTON = ('//p[normalize-space(text())="', '"]/..//button')

    def __init__(self, base_url: str, playwright_page):
        super().__init__(base_url, playwright_page)
        self._cart = Cart(playwright_page)

    @step("Open shop page")
    def open(self):
        with step(f'Go to url {self._base_url}'):
            self._page.goto(self._base_url)

    @step('Add the product "{product_name}" to the cart')
    def add_product_to_cart(self, product_name: str):
        try:
            with step('Tap on the product button'):
                self._page.click(f'{self._PRODUCT_BUTTON[0]}{product_name}{self._PRODUCT_BUTTON[1]}')
        except TimeoutError as e:
            assert False, f'Product "{product_name}" not found, error: {e}'

    @property
    def cart(self) -> Cart:
        return self._cart
