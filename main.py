import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker = SandwichMaker(resources)
cashier = Cashier()


def main():
    while True:
        user_input = input(
            "What would you like? (small/ medium/ large/ off/ report): ")

        if user_input == "off":
            break

        if user_input == "report":
            sandwich_maker.show_report()

        small_size = "small"
        medium_size = "medium"
        large_size = "large"

        if user_input in (small_size, medium_size, large_size):
            sandwich_size = user_input

            size_dict = recipes[sandwich_size]
            ingredients_dict = size_dict["ingredients"]

            is_enough_resources = sandwich_maker.check_resources(
                ingredients_dict)

            if is_enough_resources:
                amt_money = cashier.process_coins()
                sandwich_cost = size_dict["cost"]

                if cashier.transaction_result(amt_money, sandwich_cost):
                    sandwich_maker.make_sandwich(sandwich_size,
                                                 ingredients_dict)


if __name__ == "__main__":
    main()
