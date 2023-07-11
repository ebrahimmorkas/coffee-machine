water = 300
milk = 200
coffee = 100
money_in_coffee_machine = {
    "10": 10,
    "20": 10,
    "50": 5,
    "100": 5,
    "200": 3
}

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
    # print(f"$: {money}")

# Function that will add the resources in the machine
def add_resource(get_milk, get_water, get_coffee):
    global milk
    global water
    global coffee
    milk = milk + get_milk
    water = water + get_water
    coffee = coffee + get_coffee

while True:
    user_choice = input("What would you like (espresso/latte/cappuccino) or enter 'report' to know the available ingredients or enter 'add' to add the resources\n")
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

            # Creating the list that will contain the number of notes entered by user when asked
            number_of_notes_entered = []

            # Creating the variable that will keep track of total money entered by user
            total = 0

            money_input = input("Enter how many coins or notes of RS 10 you have entered")
            number_of_notes_entered.append(int(money_input))
            total = total + 10 * int(money_input)
            money_input = input("Enter how many coins or notes of RS 20 you have entered")
            total = total + 20 * int(money_input)
            number_of_notes_entered.append(int(money_input))
            money_input = input("Enter how many notes of RS 50 you have entered")
            total = total + 50 * int(money_input)
            number_of_notes_entered.append(int(money_input))
            money_input = input("Enter how many notes of RS 100 you have entered")
            total = total + 100 * int(money_input)
            number_of_notes_entered.append(int(money_input))
            money_input = input("Enter how many notes of RS 200 you have entered")
            total = total + 200 * int(money_input)
            number_of_notes_entered.append(int(money_input))

            # Checking whether the amount entered by user exactly matches the amount of coffee
            if total == menu[user_choice]['cost']:
                print("Exact money entered")

                # Iterating the dictionary that contains the amount of each note present in the machine and them updating it when user has entered the money that is increasing the amount of notes by number of notes entered by the user
                iterator = 0
                for i in money_in_coffee_machine:
                    money_in_coffee_machine[i] = money_in_coffee_machine[i] + number_of_notes_entered[iterator]
                    iterator = iterator + 1
            elif total > menu[user_choice]['cost']:
                money_remaining = total - menu[user_choice]['cost']
                print(f"Take your change {money_remaining}")
            else:
                print("You dont have enough money")
        else:
            # Resources are not available
            print("Resources Not available")
    elif user_choice == 'add':
        # print("You can add the resources")
        add_water = int(input("Please enter the amount of water you want to add in ml\n"))
        add_coffee = int(input("Please enter the amount of coffee you want to add in g\n"))
        add_milk = int(input("Please enter the amount of milk you want to add in ml\n"))
        add_resource(add_milk, add_water, add_coffee)
    else:
        print("Coffee not available")
