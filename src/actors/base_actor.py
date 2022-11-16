from playwright.sync_api import BrowserContext, Page

from src.pages.shop_page import ShopPage


class BaseActor:
    def __init__(self, base_url: str, browser_context: BrowserContext):
        self._page: Page = browser_context.new_page()
        self._shop_page: ShopPage = ShopPage(base_url=base_url, playwright_page=self._page)
