from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from pprint import pprint


coffee_maker_object = CoffeeMaker()
menu_object = Menu()
money_machine_object = MoneyMachine()

#menu_item_object = MenuItem()
is_off = 0
while is_off == 0:
    user_choice = input(f"What would you like? ({menu_object.get_items()}): ").lower()

    if user_choice == "report":
        coffee_maker_object.report()
        money_machine_object.report()

    elif user_choice == "off":
        is_off = 1
        print("shutting down machien")

    else:
        drink_selected = menu_object.find_drink(user_choice)
        # menu_item_object = MenuItem(drink_selected.name, drink_selected.water, drink_selected.coffee,
        #                             drink_selected.cost)

        # print(drink_selected.name)
        # print(drink_selected.cost)
        # print(drink_selected.ingredients['water'])
        # print(drink_selected.ingredients['milk'])
        # print(drink_selected.ingredients['coffee'])

        name = drink_selected.name
        cost = drink_selected.cost
        water = drink_selected.ingredients["water"]
        milk = drink_selected.ingredients["milk"]
        coffee = drink_selected.ingredients["coffee"]

        # print("LIST OF VARIABLE VALUES OF COFFEE DRINK SELECTED:")
        # print(f"NAME: {name}")
        # print(f"COST: {cost}")
        # print(f"WATER: {water}")
        # print(f"MILK: {milk}")
        # print(f"COFFEE:  {coffee}")

        menu_item_object = MenuItem(name, water, milk, coffee, cost)

        # pprint(vars(menu_item_object))

        is_enough_resources = coffee_maker_object.is_resource_sufficient(menu_item_object)

        # print(is_enough_resources)
        if is_enough_resources:
            if money_machine_object.make_payment(cost):
                print('MAKING COFFEE!:')
                coffee_maker_object.make_coffee(menu_item_object)
            #print('MAKING CHANGE!')
            #money_machine_object.process_coins()


