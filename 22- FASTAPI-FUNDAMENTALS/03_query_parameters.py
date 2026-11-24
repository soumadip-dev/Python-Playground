from fastapi import FastAPI
from typing import Optional

app = FastAPI()

products = [
    {"product_id": 1, "name": "Laptop", "category": "electronics", "price": 65000},
    {"product_id": 2, "name": "Headphones", "category": "electronics", "price": 2500},
    {"product_id": 3, "name": "Shoes", "category": "fashion", "price": 1800},
    {"product_id": 4, "name": "Watch", "category": "fashion", "price": 3500},
    {"product_id": 5, "name": "Book", "category": "education", "price": 500},
]


@app.get("/products")
def get_products(
    category: Optional[str] = None,
    min_price: float = 0,
    max_price: Optional[float] = None,
):
    filtered_products = []

    for product in products:
        if category is not None and product["category"] != category:
            continue

        if product["price"] < min_price:
            continue

        if max_price is not None and product["price"] > max_price:
            continue

        filtered_products.append(product)

    return {
        "message": "Products retrieved successfully.",
        "data": {
            "filters": {
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
            },
            "products": filtered_products,
        },
    }
