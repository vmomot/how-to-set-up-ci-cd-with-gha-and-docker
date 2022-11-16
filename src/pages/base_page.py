from playwright.sync_api import Page


class BasePage:
    def __init__(self, base_url: str, playwright_page: Page):
        self._base_url: str = base_url
        self._page: Page = playwright_page
