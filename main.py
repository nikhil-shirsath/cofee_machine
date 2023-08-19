import machine_menu

is_on= True

user_ask =input("What would you like? (espresso/latte/cappuccino): ")

# #TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def resource_sufficient(req_milk =0, req_water=0, req_coffee=0):
    """ This function is used to check the resources to make  coffee   """

    avalable_coffee = machine_menu.resources['coffee']
    avalable_milk = machine_menu.resources['milk']
    avalable_water = machine_menu.resources['water']
    if (avalable_water <req_water):
        print("Sorry there is not enough water.")
    elif (avalable_milk <req_milk):
        print("Sorry there is not enough milk.")
    elif(avalable_coffee <req_coffee):
        print("Sorry there is not enough coffee.")
    else:
        return True

    print(f"{avalable_coffee} {avalable_water} {avalable_milk}")



# resource_sufficient(22,22,22)

# Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52




if (user_ask =='espresso'):
    #do something
    espresso_path =machine_menu.MENU['espresso']['ingredients']
    resource_sufficient( req_water= espresso_path['water'],
                            req_coffee=espresso_path['coffee']) 
 
    print(espresso_path['water'])


elif(user_ask =="latte"):

    latte_path =machine_menu.MENU['latte']['ingredients']
    resource_sufficient(req_milk=latte_path['milk'], 
                        req_water= latte_path['water'], 
                        req_coffee=latte_path['coffee'])

    print("latte")


elif(user_ask =="cappuccino"):
    cappuccino_path =machine_menu.MENU['cappuccino']['ingredients']
    resource_sufficient(req_milk=cappuccino_path['milk'],
                         req_water= cappuccino_path['water'], 
                         req_coffee=cappuccino_path['coffee'])
    print("cappuccino")

elif(user_ask =="off"):
    is_on==False

elif(user_ask =="report"):
    print(f"Water : {machine_menu.resources['water']}ml\nMilk : {machine_menu.resources['milk']}ml\nCoffee: {machine_menu.resources['coffee']}g")
    

# TODO 1 : Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

#TODO :3. 3. Print report.
 # a. When the user enters “report” to the prompt, a report should be generated that shows
 # the current resource values. e.g.
 # Water: 100ml
 # Milk: 50ml
 # Coffee: 76g
 # Money: $2.5

# TODO : 2. Turn off the Coffee Machine by entering “off” to the prompt.
 # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
 # the machine. Your code should end execution when this happens.