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
profit=0

show_again=True

# #TODO :4Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. 
# It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee

def resource_sufficient(drink, resources):
    # print(drink)
    # print(resources)
    for item in drink :
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            is_sufficient=True
    return is_sufficient


# #TODO:5  Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins():
    if(resource_sufficient(drink=drink,resources=resources)):
        print(" \n\nPlease Insert coins \n\n")
        user_coins =int(input("insert quarters "))
        user_coins =int(input("insert dimes "))
        user_coins =int(input("insert nickles "))
        user_coins =int(input("insert pennies "))
        





while show_again:
    user_choice =input(" What would you like? espresso/latte/cappuccino: ")

    if user_choice=="off" or user_choice=="OFF":
        show_again=False
    elif user_choice=="report":
        print(f" water : {resources['water']} \n milk : {resources['milk']} \n coffee : {resources['coffee']} " )
    else:
        drink =MENU[user_choice]
        # print(drink)
        print(resource_sufficient(drink=drink['ingredients'],resources=resources))