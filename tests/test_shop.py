from allure import title


class TestShop:

    @title("The customer can add a product to the cart and checkout it")
    def test_customer_can_checkout_the_product(self, shop_page):
        shop_page.open()
        shop_page.add_product_to_cart('Cropped Stay Groovy off white')
        shop_page.cart.tap_on_checkout_button()
        shop_page.cart.check_that_checkout_alert_is_present()
