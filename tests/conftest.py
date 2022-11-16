from pytest import fixture

from config import Config
from src.pages.shop_page import ShopPage


@fixture(scope='session', autouse=True)
def config() -> Config:
    config = Config()
    return config


# @fixture
# def customer(config, context) -> CustomerActor:
#     customer = CustomerActor(base_url=config.base_url,
#                              browser_context=context)
#     return customer


@fixture
def shop_page(config, page) -> ShopPage:
    page = ShopPage(base_url=config.base_url, playwright_page=page)
    return page
