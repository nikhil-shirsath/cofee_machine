import machine_menu


# TODO 1 : Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
is_on= True

while is_on:

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "espresso":

        #do this
    elif user_input== "latte":

        #do this
    elif user_input== "cappuccino" :

        #do this
    elif user_input== "report":
        #TODO :3. 3. Print report.
        # a. When the user enters “report” to the prompt, a report should be generated that shows
        # the current resource values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        print(f"Water {machine_menu.resources.get("water") }\nMilk: {machine_menu.resour}\nCoffee: {}\nMoney: ${}")

    # TODO : 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    elif user_input == "off" :
        is_on=False