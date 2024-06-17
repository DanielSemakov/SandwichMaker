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


### Make an instance of SandwichMachine class and write the rest of the codes ###
git ad