from menu import MENU
from menu import resources
from art import logo

menu = MENU
coins = {
    "quarter": 0.25,
    "dimes": 0.1,
    "nickel": 0.05,
    "pennies": 0.01,
    "euro": 1
}

def coffee_choice(type, report):
    """La funcion da la informacion necesaria al usuario
        y devuelvel la cantidad que debe introducir"""
    price = 0
    if type == "report":
        for key, value in report.items():
            print(f"resource left {key} -> {value}")
    elif type == "expresso":
        print(f"insert coin -> {MENU['espresso']['cost']}")
        price = MENU['espresso']['cost']
    elif type == "latte":
        print(f"insert coin-> {MENU['latte']['cost']}")
        price = MENU['latte']['cost']
    elif type == "cappuccino":
        print(f"insert coin-> {MENU['cappuccino']['cost']}")
        price = MENU['cappuccino']['cost']
    elif type == "off":
        print(f"The coffee machine will turn off")
    else:
        print("the product does not exist")
    return price

def detect_coin(money):
    for name, value in coins.items():
        if money == name:
            print(f"Correct coin {coins[name]}")
            return coins[name]


def insert_coin(money_total):
    money = str(input("Insert coin: quarter/dimes/nickel/pennies: "))
    if money != "quarter" and money != "dimes" and money != "nickel" and money != "pennies" and money != "euro":
        print("there is not enough money")
        return -1
    coin = detect_coin(money)
    money_total += coin
    return money_total

print(logo)
flag = 1
report = resources
while flag == 1:
    money_total = 0.0
    money = 0
    type = str(input("What would you like? (expresso/latte/capuccino)"))
    if type == "off":
        flag = 0
    price = coffee_choice(type, report)
    while price > money_total:
        money_total = insert_coin(money_total)
        if money_total == -1:
            break
        print(f"money = {money_total}")
        if price <= money_total:
            print(f"your {type} thank you")
            if price < money_total:
                money = money_total - price
                print(f"your change thank you {money:.2f}")
            for material, value in report.items():
                for tipo, cost in menu.items():
                    if type == tipo:
                        report['water'] -= menu[tipo]['ingredients']['water']
                        report['milk'] -= menu[tipo]['ingredients']['milk']
                        report['coffee'] -= menu[tipo]['ingredients']['coffee']


# TODO Hacer una funcion para detectar monedas y sumarlas a la cantidad total
