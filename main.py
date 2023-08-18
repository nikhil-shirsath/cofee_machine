import machine_menu

is_on= True

user_ask =input("What would you like? (espresso/latte/cappuccino): ")

if (user_ask =='espresso'):
    #do something
    print("hellow")
elif(user_ask =="latte"):
    print("latte")
elif(user_ask =="cappuccino"):
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