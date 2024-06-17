class Cashier:
    def __init__(self):
        pass

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

