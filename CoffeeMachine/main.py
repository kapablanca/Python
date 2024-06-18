MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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


def calculate_price(item):
    """ Takes as an input the item from MENU and returns its cost"""
    price = MENU[item]["cost"]
    return price


def calculate_resources(item):
    """Returns the resources you need based on the coffee you selected"""
    resources_needed = MENU[item]["ingredients"]
    return resources_needed


def insert_money(quarter, dime, nickle, penny):
    """Calculates the total money you inserted in the coffee machine"""
    value = {
        "quarter": 0.25,
        "dime": 0.10,
        "nickle": 0.05,
        "penny": 0.01
    }
    total_money = quarter * value["quarter"] + dime * value["dime"] + nickle * value["nickle"] \
                  + penny * value["penny"]
    return total_money


def check_resources(ingredients, resources_left):
    """Takes as input the dictionary of ingredients needed for a coffee and the resources left
    to make a coffee and returns if it can be made or not"""
    is_enough = True
    for amount in resources_left["ingredients"]:
        if resources_left["ingredients"][amount] < ingredients[amount]:
            return amount
    return is_enough


def add_resources(inventory, needed):
    """Remove the ingredients needed and calculate the final inventory"""
    new_resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0
        }
    for item in inventory["ingredients"]:
        new_resources[item] = inventory["ingredients"][item] - needed[item]
    return new_resources


def show_inventory(inventory):
    print(f"Water: {inventory['ingredients']['water']}ml")
    print(f"Milk: {inventory['ingredients']['milk']}ml")
    print(f"Coffee: {inventory['ingredients']['coffee']}g")
    print(f"Money: ${inventory['money']}")


def coffee_maker():
    turn_off = False
    resources = {
        "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            },
        "money": 0
        }

    while not turn_off:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            return
        elif choice == "report":
            show_inventory(resources)
        else:
            needed_ingredients = calculate_resources(choice)
            enough = check_resources(needed_ingredients, resources)
            if isinstance(enough, str):
                print(f"Sorry there is not enough {enough}")
            else:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                coins_inserted = insert_money(quarters, dimes, nickles, pennies)
                item_price = calculate_price(choice)
                if coins_inserted >= item_price:
                    resources["money"] += item_price
                    change = round((coins_inserted-item_price), 2)
                    resources["ingredients"] = add_resources(resources, needed_ingredients)
                    print(f"Here is ${change} dollars in change.")
                    print(f"Here is your {choice} ☕.Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded")


coffee_maker()
