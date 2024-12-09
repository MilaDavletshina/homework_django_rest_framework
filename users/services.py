import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    """Создание цены в stripe."""
    stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "Payments"},
    )


def create_stripe_product(product):
    """Создание продукта в stripe."""
    stripe.Product.create(name=product)


def create_stripe_sessions(price):
    """Создание сессии в stripe."""
    sessions = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return sessions.get("id"), sessions.get("url")
