from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()

                  # MINE
# while True:
#     payment =0
#     user_order = input(f"What would you like? ({menu.get_items()}): ")
#     if user_order == "report":
#         coffee_maker.report()
#         money_machine.report()
#         continue
#     elif user_order == "off":
#         break
#
#     order_info= menu.find_drink(user_order)
#
#     if coffee_maker.is_resource_sufficient(order_info):
#         money_machine.make_payment(order_info.cost)
#
#     coffee_maker.make_coffee(order_info)


#Better way to workflow
is_on = True
while is_on:
    options = menu.get_items()
    choice =input(f"What would you like? ({options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) :
            coffee_maker.make_coffee(drink)
