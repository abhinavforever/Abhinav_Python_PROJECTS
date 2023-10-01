def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
w = 300
m = 200
c = 100
p = 0
money=0
flag = True
# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
while flag:
    a = input("What would you like?")

    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if a == 'off':
        flag = False


    # TODO 3. Print report.
    elif a == "report":
        print(f"Water: {w}\nMilk: {m}\nCoffee: {c}\nMoney: {money}")

    # TODO 4. Check resources sufficient?
    elif a in MENU.keys():
        if a == "espresso":
            if w >= MENU[a]['ingredients']['water'] and c >= MENU[a]['ingredients']['coffee']:
                # TODO 5. Process coins.
                print("insert coins: q, d, n, p = 0.25, 0.1, 0.05, 0.01")
                q, d, n, p = 0.25, 0.1, 0.05, 0.01
                nq, nd, nn, np = 0, 0, 0, 0
                flag2 = True
                while flag2:
                    coin = input()
                    if isfloat(coin)==True:
                        if float(coin) == 0.25:
                            nq += 1
                        elif float(coin) == 0.1:
                            nd += 1
                        elif float(coin) == 0.05:
                            nn += 1
                        elif float(coin) == 0.01:
                            np += 1

                    else:
                        flag2 = False
                total_inserted = nq * q + nd * d + nn * n + np * p

                # TODO 6. Check transaction successful?
                # a. Check that the user has inserted enough money to purchase the drink they selected.
                # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
                # program should say “ Sorry that's not enough money. Money refunded. ”.
                # b. But if the user has inserted enough money, then the cost of the drink gets added to the
                # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
                # Water: 100ml
                # Milk: 50ml
                # Coffee: 76g
                # Money: $2.5
                # c. If the user has inserted too much money, the machine should offer change.
                # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
                # places.

                if total_inserted >= MENU[a]['cost']:
                    print(f"Here is your {a}. Enjoy!")
                    money+=MENU[a]['cost']
                    w = w - MENU[a]['ingredients']['water']
                    c = c - MENU[a]['ingredients']['coffee']
                    p += MENU[a]['cost']
                    if total_inserted > MENU[a]['cost']:
                        change = total_inserted - MENU[a]['cost']
                        change = round(change, 2)
                        print(f"Here is ${change} dollars in change")
                else:
                    print("sorry that's not enough money.Money refunded")
            elif w < MENU[a]['ingredients']['water'] or c < MENU[a]['ingredients']['coffee']:
                if w < MENU[a]['ingredients']['water']:
                    print("sorry not enough water")
                if c < MENU[a]['ingredients']['coffee']:
                    print("sorry not enough coffee")
        else:
            if w >= MENU[a]['ingredients']['water'] and c >= MENU[a]['ingredients']['coffee'] and m >= \
                    MENU[a]['ingredients']['milk']:
                print("insert coins: q, d, n, p = 0.25, 0.1, 0.05, 0.01")
                q, d, n, p = 0.25, 0.1, 0.05, 0.01
                nq, nd, nn, np = 0, 0, 0, 0
                flag2 = True
                while flag2:
                    coin = input()
                    if isfloat(coin)==True:
                        if float(coin) == 0.25:
                            nq += 1
                        elif float(coin) == 0.1:
                            nd += 1
                        elif float(coin) == 0.05:
                            nn += 1
                        elif float(coin) == 0.01:
                            np += 1
                    else:
                        flag2 = False
                total_inserted = nq * q + nd * d + nn * n + np * p
                if total_inserted >= MENU[a]['cost']:
                    print(f"Here is your {a}. Enjoy!")
                    money+=MENU[a]['cost']
                    w = w - MENU[a]['ingredients']['water']
                    c = c - MENU[a]['ingredients']['coffee']
                    m = m - MENU[a]['ingredients']['milk']
                    if total_inserted > MENU[a]['cost']:
                        change = total_inserted - MENU[a]['cost']
                        change = round(change, 2)
                        print(f"Here is ${change} dollars in change")
                else:
                    print("sorry that's not enough money.Money refunded")
            elif w < MENU[a]['ingredients']['water'] or c < MENU[a]['ingredients']['coffee'] or m < \
                    MENU[a]['ingredients']['milk']:
                if w < MENU[a]['ingredients']['water']:
                    print("sorry not enough water")
                if c < MENU[a]['ingredients']['coffee']:
                    print("sorry not enough coffee")
                if m < MENU[a]['ingredients']['milk']:
                    print("sorry not enough milk")
