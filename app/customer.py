import math

from app.car import Car
from app.data import Data
from app.shop import Shop


class Customer:
    group_customers: list["Customer"] = []

    def __init__(
        self, **data
    ) -> None:
        self.name = data.get("name")
        self.product_cart = data.get("product_cart")
        self.location = data.get("location")
        self.money = data.get("money")
        self.car = Car(
            data.get("car").get("brand"),
            data.get("car").get("fuel_consumption"))

    def calculate_cost(self, shop: Shop) -> float:
        x, y = self.location
        x1, y1 = shop.location
        distance = math.sqrt(((x1 - x) ** 2) + ((y1 - y) ** 2))

        car_cost_there_and_back = (
            (
                (self.car.fuel_consumption * distance) / 100
            )
            * Data.data["FUEL_PRICE"] * 2
        )
        products_sum_price = 0
        for product, count in self.product_cart.items():
            products_sum_price += shop.products.get(product, 0) * count

        return round((car_cost_there_and_back + products_sum_price), 2)

    @classmethod
    def generate_unit(cls) -> None:
        for unit in Data.data["customers"]:
            customer = Customer(**unit)
            cls.group_customers.append(customer)


class NotEnoughMoneyException(Exception):
    """Custom exception for cases when customer doesn't have enough money"""
