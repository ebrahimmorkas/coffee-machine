water = 300
milk = 200
coffee = 100
money = 0

menu = {
    "espresso": {
        "ingredients": {
            "milk": 100,
            "water": 50,
            "coffee": 50
        },
        "cost": 100
    },

    "latte": {
        "ingredients": {
            "milk": 50,
            "water": 100,
            "coffee": 100
        },
        "cost": 200
    },

    "cappuccino": {
        "ingredients": {
            "milk": 150,
            "water": 50,
            "coffee": 150
        },
        "cost": 200
    }
}

def available_resources():
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee} g")
    print(f"$: {money}")

while True:
    user_choice = input("What would you like (espresso/latte/cappuccino) or enter 'report' to know the available ingredients\n")
    if user_choice == 'report':
        available_resources()
