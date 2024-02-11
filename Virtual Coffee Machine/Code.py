Menu = {
    "Latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 150
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 200
    }
}

profit = 0
resources = {"Water": 500, "Milk": 200, "Coffee": 100}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coin.")
    total=0
    coin_five=int(input("How many 5rs coin?: "))
    coin_ten=int(input("How many 10rs coin?: "))
    coin_twenty=int(input("How many 20rs coin?: "))
    total=coin_five*5 + coin_ten*10 + coin_twenty*20
    return total

def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change= money_received-coffee_cost
        print(f"Here is your Rs{change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
def make_coffee(coffee_name,coffee_ingredient):
    for item in coffee_ingredient:
        resources[item]-=coffee_ingredient[item]
    print(f"Here is your {coffee_name}☕︎... Enjoy!!")
    
is_on = True

while is_on:
    choice = input("Hello! What would you like to have?\nLatte, espresso, cappuccino.\n")
    if choice == "off":
        is_on = False
        print("Machine is turned off!!")
    elif choice == "report":
        print(f"water={resources['Water']}ml")
        print(f"milk={resources['Milk']}ml")
        print(f"coffee={resources['Coffee']}ml")
        print(f"money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
