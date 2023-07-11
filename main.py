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
        "cost": 300
    }
}

# List that will contain all the names of available coffees
available_coffees = ['espresso', 'latte', 'cappuccino']

def available_resources():
    print(f"Water: {water} ml")
    print(f"Milk: {milk} ml")
    print(f"Coffee: {coffee} g")
    print(f"$: {money}")

while True:
    user_choice = input("What would you like (espresso/latte/cappuccino) or enter 'report' to know the available ingredients\n")
    if user_choice == 'report':
        available_resources()
    elif user_choice in available_coffees:
        # print("Coffee Available")
        # print(menu["latte"]['ingredients']['milk'])

        # Checking whether the resources are available
        if menu[user_choice]['ingredients']['milk'] <= milk and menu[user_choice]['ingredients']['water'] <= water and menu[user_choice]['ingredients']['coffee'] <= coffee:
            # Resources are available
            # print("Resources Available")
            milk = milk - menu[user_choice]['ingredients']['milk']
            water = water - menu[user_choice]['ingredients']['water']
            coffee = menu[user_choice]['ingredients']['coffee']

            print(f"Latte will cost {menu[user_choice]['cost']}")
        else:
            # Resources are not available
            print("Resources Not available")
    else:
        print("Coffee not available")
