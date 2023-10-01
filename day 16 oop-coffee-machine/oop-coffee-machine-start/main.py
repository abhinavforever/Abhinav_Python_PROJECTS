from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m=Menu()
co=CoffeeMaker()
mo=MoneyMachine()

flag=True
while flag:
    u=input(f"Make your choice {m.get_items()} ")
    if u=="off":
        flag=False
    elif u=="report":
        mo.report()
        co.report()
    else:
        if m.find_drink(u)!=None:
            drink=m.find_drink(u)
            if co.is_resource_sufficient(drink) and mo.make_payment(drink.cost):
                co.make_coffee(drink)