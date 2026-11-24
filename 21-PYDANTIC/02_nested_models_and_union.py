from typing import Union
from pydantic import BaseModel


# Nested Model 1
class Address(BaseModel):
    street: str
    city: str
    zip_code: str


# Nested Model 2
class Product(BaseModel):
    name: str
    price: float


class CardPayment(BaseModel):
    card_number: str
    card_holder: str


class UpiPayment(BaseModel):
    upi_id: str


# Main Model
class Order(BaseModel):
    order_id: int
    delivery_address: Address
    product: Product
    payment: Union[CardPayment, UpiPayment]


order_data = {
    "order_id": 101,
    "delivery_address": {
        "street": "123 Main Street",
        "city": "Kolkata",
        "zip_code": "700001",
    },
    "product": {"name": "Wireless Headphones", "price": 2499.99},
    "payment": {"upi_id": "soumadip@upi"},
}

order = Order(**order_data)

print(order)
print(order.model_dump())