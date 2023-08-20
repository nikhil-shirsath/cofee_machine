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
    """This function takes drink ingredeants and resouces available and returns True if resources are available,
    otherwise it returns false ."""
    for item in drink :
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        
    return True


# #TODO:5  Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins():
    """ This function calculates coins and change them into the $ dollers 
    returns total dollers."""
    user_total_coins=0
    print(" \n\nPlease Insert coins \n\n")
    user_toatal_coins =int(input("insert quarters "))*0.25
    user_total_coins +=int(input("insert dimes "))*0.10
    user_total_coins +=int(input("insert nickles "))*0.05
    user_total_coins +=int(input("insert pennies "))*0.01    
    return user_total_coins 

def is_transection_successful(money_recieved,drink_cost):
    """Return true if payment is accepted or return false if payment is denied 
    and refunds money."""
    if money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        global profit
        profit += drink_cost
        change_money = round(money_recieved - drink_cost,2)
        print(f"Here is $.{change_money} dollars in change.")
        return True


def make_coffee(coffee_ingredients, resources):
    for item in coffee_ingredients:
        resources[item] -=coffee_ingredients[item]
    return True




while show_again:
    user_choice =input(" What would you like? espresso/latte/cappuccino: ")

    if user_choice=="off" or user_choice=="OFF":
        show_again=False
    elif user_choice=="report":
        print(f" water : {resources['water']} \n milk : {resources['milk']} \n coffee : {resources['coffee']} \n collection ${profit} " )
    elif user_choice=="espresso" or user_choice =="latte" or user_choice=="cappuccino":
        drink =MENU[user_choice]
        # print(drink)
        if (resource_sufficient(drink=drink['ingredients'],resources=resources)):
            money_recieved = process_coins()
            trasection = is_transection_successful(money_recieved=money_recieved, drink_cost=drink['cost'])
            if trasection:
               coffee_done = make_coffee(coffee_ingredients=drink['ingredients'],resources=resources)
               if coffee_done:
                   print(f"Here is your {user_choice}. Enjoy!.")
    else:
        print("Enter proper option. ")