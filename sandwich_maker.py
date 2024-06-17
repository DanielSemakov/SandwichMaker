class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

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