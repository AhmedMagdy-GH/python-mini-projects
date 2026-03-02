menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

# TODO: 1.Ask user for what he want.
def get_user_choice():
    """Ask the user for a drink and validate the input."""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choice not in menu and choice not in ["report", "off"]:
        choice = input("Enter a valid option: ").lower()
    return choice

# TODO: 2.Print report.
def print_report(money):
    """Take money as parameter and print report"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${money}")


# #TODO: 3.Build check_resources function.
def check_resources(user_order):
    for order in user_order:
        if user_order[order] >= resources[order]:
            print(f"Sorry there is not enough {order}.")
            return False

    return True


#TODO: 4.Process coins.
def calculate_coins():
    """Calculate the amount paid by customer and return it"""
    amount = 0
    amount+= int(input("How many quarters?: ")) *coins["quarter"]
    amount+= int(input("How many dimes?: ")) *coins["dime"]
    amount+= int(input("How many nickels?: ")) *coins["nickel"]
    amount+= int(input("How many pennies?: ")) *coins["penny"]
    return amount


#TODO: 5.Make transaction_successful function.
def transaction_successful(money, amount, user_order):
    """Check transaction and return money, continue order """
    if amount >= menu[user_order]["cost"]:
            money += menu[user_order]["cost"]
            change = amount - menu[user_order]["cost"]
            if change >0:
                print(f"Here is ${round(change,2)} dollars in change")
            return money, True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return money, False


#TODO: 6.Build Make_order function.
def make_order(drink_name, order_ingredients):
    """Make the order and update resources using a loop"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}☕. Enjoy!")


def run_machine():
    """The main function"""
    money = 0
    user_order =""

    while user_order != "off":

        user_order = get_user_choice()

        if user_order == "report":
            print_report(money)
            continue

        # TODO: 7.Turn off the coffee machine by entering "off" to the prompt.
        if  user_order == "off":
            return

        elif not check_resources(menu[user_order]["ingredients"]):
            continue

        amount = calculate_coins()
        money, continue_order = transaction_successful(money, amount, user_order)

        if not continue_order:
            continue

        make_order(user_order, menu[user_order]["ingredients"])

run_machine()