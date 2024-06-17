### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###
class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients) -> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""

        bread_ingred = "bread"
        if ingredients[bread_ingred] > self.machine_resources[bread_ingred]:
            print(f"Sorry there is not enough {bread_ingred}.")
            return False

        ham_ingred = "ham"
        if ingredients[ham_ingred] > self.machine_resources[ham_ingred]:
            print(f"Sorry there is not enough {ham_ingred}.")
            return False

        cheese_ingred = "cheese"
        if ingredients[cheese_ingred] > self.machine_resources[cheese_ingred]:
            print(f"Sorry there is not enough {cheese_ingred}.")
            return False

        return True

    def process_coins(self) -> float:
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")

        numDollars = int(input("How many large dollars?: "))
        numHalfDollars = int(input("How many half dollars?: "))
        numQuarters = int(input("How many quarters?: "))
        numNickels = int(input("How many nickels?: "))

        return numDollars + 0.5 * numHalfDollars + 0.25 * numQuarters + 0.05 * numNickels

    def transaction_result(self, coins, cost) -> bool:
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            amt_change = coins - cost
            print(f"Here is ${amt_change:.2f} in change.")
            return True
        else:
            print("Sorry, that’s not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients) -> None:
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        bread_ingred = "bread"
        ham_ingred = "ham"
        cheese_ingred = "cheese"

        self.machine_resources[bread_ingred] -= order_ingredients[bread_ingred]
        self.machine_resources[ham_ingred] -= order_ingredients[ham_ingred]
        self.machine_resources[cheese_ingred] -= order_ingredients[
            cheese_ingred]

        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def show_report(self):
        bread_ingred = "bread"
        ham_ingred = "ham"
        cheese_ingred = "cheese"

        amt_bread = self.machine_resources[bread_ingred]
        amt_ham = self.machine_resources[ham_ingred]
        amt_cheese = self.machine_resources[cheese_ingred]

        print(f"{bread_ingred.capitalize()}: {amt_bread} slice(s)")
        print(f"{ham_ingred.capitalize()}: {amt_ham} slice(s)")
        print(f"{cheese_ingred.capitalize()}: {amt_cheese} ounce(s)")

def main():
    while True:
        user_input = input(
            "What would you like? (small/ medium/ large/ off/ report): ")

        if user_input == "off":
            break

        sandwich_machine = SandwichMachine(resources)

        if user_input == "report":
            sandwich_machine.show_report()

        small_size = "small"
        medium_size = "medium"
        large_size = "large"

        if user_input in (small_size, medium_size, large_size):
            sandwich_size = user_input

            size_dict = recipes[sandwich_size]
            ingredients_dict = size_dict["ingredients"]

            is_enough_resources = sandwich_machine.check_resources(
                ingredients_dict)

            if is_enough_resources:
                amt_money = sandwich_machine.process_coins()

                sandwich_dict = recipes[sandwich_size]
                sandwich_cost = sandwich_dict["cost"]

                if sandwich_machine.transaction_result(amt_money,
                                                       sandwich_cost):
                    sandwich_machine.make_sandwich(sandwich_size,
                                                   ingredients_dict)


if __name__ == "__main__":
    main()
