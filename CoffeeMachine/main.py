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

def want_coffee(flag):
    """guarda el tipo de cafe en una variable y guarda en flag la desicion tomada
    1 = cafe elegido/2 = recursos/-1 = error"""
    type_coffee = input("what coffee do you want?(espresso/latte/cappuccino)")
    if type_coffee == MENU["espresso"] or type_coffee == MENU["latte"] or type_coffee == MENU["cappuccino"]
        flag == 1
    elif type_coffee == "report":
        flag == 2
    else:
        flag = -1
    return flag

