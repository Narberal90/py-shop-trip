import json

from app.customer import Customer
from app.data import Data
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        Data.data = json.load(file)

    Customer.generate_unit()
    Shop.generate_shop()

    for customer in Customer.group_customers:
        print(f"{customer.name} has {customer.money} dollars")

        shop_choice = [None, float("inf")]

        for shop in Shop.shop_list:
            trip_calculate = customer.calculate_cost(shop)
            if trip_calculate < shop_choice[1]:
                shop_choice[1] = trip_calculate
                shop_choice[0] = shop

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_calculate}")

        money_change = customer.money - shop_choice[1]
        if money_change < 0:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop"
                  )
            return

        print(f"{customer.name} rides to {shop_choice[0].name}")

        shop_choice[0].get_service(customer)

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {round(money_change, 2)} dollars\n")
