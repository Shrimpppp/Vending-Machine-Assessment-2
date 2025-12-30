# global variables
wallet = 0

# items, stocks and prices
snacks_dict = {
    0: {"name": "Chips", "price": 1.50, "stock": 1 , "sugg": "Coke / Pepsi / Peached Ice Tea / Lemon Ice Tea"},
    1: {"name": "Reese's", "price": 2.00, "stock": 3, "sugg": "Chocolate Milk / Vanilla Cold Brew"},
    2: {"name": "Malteesers", "price": 2.75, "stock": 4, "sugg": "Chocolate Milk"},
    3: {"name": "Oreo", "price": 1.25, "stock": 1, "sugg": "Chocolate milk / Caramel Cold Brew / Vanilla Cold Brew"},
    4: {"name": "Kinder Chocolate", "price": 2.00, "stock": 1, "sugg": "Chocolate milk"},
    5: {"name": "Tim Tams", "price": 1.50, "stock": 2, "sugg": "Chocolate Milk / Vanilla Cold Brew / Espresso"},
    6: {"name": "Twinkies", "price": 1.50, "stock": 2, "sugg": "Anything on the hot drinks catalogue"},
    7: {"name": "Skittles", "price": 2.25, "stock": 3, "sugg": "Chocolate milk / Water"},
    8: {"name": "M&M's", "price": 2.50, "stock": 3, "sugg": "Chocolate milk / Water"},
    9: {"name": "Takis", "price": 3.00, "stock": 1, "sugg": "Chocolate milk / Water / Lemon Ice Tea / Lemon Ice Tea"},
    10: {"name": "Skyflakes", "price": 1.00, "stock": 3, "sugg": "Anything on the Hot drinks Catalogue / Chocolate Milk"}}

cold_drinks_dict = {
    0: {"name": "Coke", "price": 2.00, "stock": 2, "sugg": "Chips / Takis"},
    1: {"name": "Chocolate Milk", "price": 3.00, "stock": 3, "sugg": "Skyflakes / Twinkies / Oreo"},
    2: {"name": "Pepsi", "price": 2.50, "stock": 4, "sugg": "Chips / Tankis"},
    3: {"name": "Cold Water", "price": 1.00, "stock": 3, "sugg": "Anything in the snack catalogue."},
    4: {"name": "Iced Latte", "price": 2.25, "stock": 4, "sugg": "Twinkies / Skyflakes"},
    5: {"name": "Vanilla Cold Brew", "price": 5.00, "stock": 1, "sugg": "Twinkies / Skyflakes"},
    6: {"name": "Caramel Cold Brew", "price": 4.00, "stock": 2, "sugg": "Twinkies / Skyflakes"},
    7: {"name": "Chocolate Cream Cold Brew", "price": 5.00, "stock": 1, "sugg": "Twinkies / Skyflakes / Tim Tams"},
    8: {"name": "Lemon Ice Tea", "price": 2.50, "stock": 3, "sugg": "Chips / Takis"},
    9: {"name": "Peached Ice Tea", "price": 2.50, "stock": 2, "sugg": "Chips / Takis."},
    10: {"name": "Chocolate Milk Shake", "price": 3.50, "stock": 3, "sugg": " Reese's / Crackers / Twinkies / Oreo / Tim Tams"}}

Hot_drinks_dict = {
    0: {"name": "Classic Hot chocolate", "price": 2.50, "stock": 2, "sugg": "Twinkies / Crackers"},
    1: {"name": "Espresso", "price": 1.50, "stock": 2, "sugg": "Twinkies / Crackers"},
    2: {"name": "Vanilla Latte", "price": 2.75, "stock": 1, "sugg": "Twinkies / Crackers"},
    3: {"name": "Mocha", "price": 3.50, "stock": 2, "sugg": "Twinkies / Crackers"},
    4: {"name": "Chamomile Tea", "price": 2.00, "stock": 3, "sugg": "Twinkies / Crackers"},
    5: {"name": "Chai Latte", "price": 1.50, "stock": 2, "sugg": "Twinkies / Crackers"},
    6: {"name": "Matcha Latte", "price": 4.75, "stock": 1, "sugg": "Twinkies / Crackers / SKyflakes"},
    7: {"name": "Dark Chocolate", "price": 1.75, "stock": 3, "sugg": "Twinkies / Crackers / Skyflakes"},
    8: {"name": "Marshmellow Hot Chocolate", "price": 2.00, "stock": 1, "sugg": "Twinkies / Crackers / Skyflakes"},
    9: {"name": "Spiced Hot Chocolate", "price": 3.00, "stock": 1, "sugg": "Twinkies / Crackers / Skyflakes"},
    10: {"name": "Green Tea", "price": 1.50, "stock": 1, "sugg": "Twinkies / Crackers / Skyflakes"}}

# func - checks if bill is valid
def money_check(m):
    try:
        money = float(m)
        if money > 20:
            print(f"Please enter a bill $20 or under. \nreturning ${money}...")
            return 0
        elif money < 1:
            print(f"Please enter  bill minimum $1\nreturning ${money}...")
            return 0
        else:
            return money
    except:
        print("This is not a bill")
        return 0


# adds hot drinks
def hot_drinks():
    global wallet
    print("here is the snack catalogue: ")
    for z in range(0,11):
        # if stock is out print "Out of stock" elif wallet > price, print in menu else print insufficient funds.
        if Hot_drinks_dict[z]["stock"] == 0:
            print("---Out of Stock---")
        elif wallet >= Hot_drinks_dict[z]["price"]:
            print(f"({z})" + Hot_drinks_dict[z]["name"] + " $" + str(Hot_drinks_dict[z]["price"]))
        else:
            print("---Insufficient Funds---")
    Hot_drink_user_opt = input("please enter the number of the snack you want, Q to quit: ")
    try: #converts users option to int
        Hot_drink_user_option = int(Hot_drink_user_opt)
        non_string = True
    except:
        non_string = False
        if Hot_drink_user_opt.upper() == 'Q':
            next
        else: 
            print("Invalid Input")
            next
            # quits if both is executed
            
    if non_string:
        if Hot_drink_user_option > 10 or Hot_drink_user_option < 0:
            print("Please select an item in the menu")
            hot_drinks()
        elif Hot_drinks_dict[Hot_drink_user_option]["stock"] < 1:
            print("Out of stock...")
        elif Hot_drinks_dict[Hot_drink_user_option]["price"] <= wallet:
            wallet -= Hot_drinks_dict[Hot_drink_user_option]["price"]
            Hot_drinks_dict[Hot_drink_user_option]["stock"] -= 1
            print(f"dispensing {Hot_drinks_dict[Hot_drink_user_option]['name']}...")# dispense, wallet balance remaining and stocks
            print(f"{Hot_drinks_dict[Hot_drink_user_option]['name']} goes well with {Hot_drinks_dict[Hot_drink_user_option]['sugg']}")
        elif wallet < Hot_drinks_dict[Hot_drink_user_option]['price']:
            print("insufficient funds...")
        else:
            print("Invalid Input")
            

# adds snacks
def snack():
    global wallet
    print("here is the snack catalogue: ")
    for i in range(0,11):
        if snacks_dict[i]['stock'] == 0:
            print("---Out of Stock---")
        elif wallet >= snacks_dict[i]['price']:
            print(f"({i})" + snacks_dict[i]["name"] + " $" + str(snacks_dict[i]["price"]))
        else: 
            print("---Insufficient Funds---")
    snack_user_opt = input("please enter the number of the snack you want, Q to quit: ")
    try:
        snack_user_option = int(snack_user_opt)
        non_string = True
    except:
        non_string = False
        if snack_user_opt.lower() == "q":
            next
        else:
            print("Invalid Input")
            next
    if non_string:
        if snack_user_option > 10 or snack_user_option < 0:
            print("Please select an item in the menu")
            snack()
        elif snacks_dict[snack_user_option]["stock"] < 1:
            print("Out of stock...")
        elif snacks_dict[snack_user_option]["price"] <= wallet:
            wallet -= snacks_dict[snack_user_option]["price"]
            snacks_dict[snack_user_option]["stock"] -= 1
            print(f"dispensing {snacks_dict[snack_user_option]['name']}...")
            print(f"{snacks_dict[snack_user_option]['name']} goes well with {snacks_dict[snack_user_option]['sugg']}")
        elif wallet < snacks_dict[snack_user_option]['price']:
            print("insufficient funds...")
        else:
            print("Invalid Input")


# adds cold drinks
def cold_drinks():
    global wallet
    print("here is the snack catalogue: ")
    for z in range(0,11):
        if cold_drinks_dict[z]['stock'] == 0:
            print("---Out of Stock---")
        elif wallet >= cold_drinks_dict[z]['price']:
            print(f"({z})" + cold_drinks_dict[z]["name"] + " $" + str(cold_drinks_dict[z]["price"]))
        else:
            print("---Insufficient Funds---")
    cold_drink_user_opt = input("Please enter the number of the cold drink you want, Q to quit: ")
    try:
        cold_drink_user_option = int(cold_drink_user_opt)
        non_string = True
    except:
        non_string = False
        if cold_drink_user_opt.lower() == 'q':
            next
        else:
            print("Invalid Input")
            next
    
    if non_string:
        if cold_drink_user_option > 10 or cold_drink_user_option < 0:
            print("Please select an item in the menu")
            cold_drinks()
        elif cold_drinks_dict[cold_drink_user_option]['stock'] < 1:
            print("Out of stock...")
        elif cold_drinks_dict[cold_drink_user_option]["price"] <= wallet:
            wallet -= cold_drinks_dict[cold_drink_user_option]["price"]
            cold_drinks_dict[cold_drink_user_option]['stock'] -= 1
            print(f"dispensing {cold_drinks_dict[cold_drink_user_option]['name']}...")
            print(f"{cold_drinks_dict[cold_drink_user_option]['name']} goes well with {cold_drinks_dict[cold_drink_user_option]['sugg']}")
        elif wallet < cold_drinks_dict[cold_drink_user_option]['price']:
            print("insufficient funds...")    
        else:
            print("Invalid Input")
            
# main block - runs all functions
print("======================VENDING MACHINE======================")
# shows minimum values per dict
print("The minimum Value for:\nHot drink = $1.50\nCold drinks = $1.00\nSnacks = $1.00")
# money check
while wallet == 0:
    wallet = money_check(input("Enter a bill not higher than 20: "))


# add to cart
while True:
    print(f"Wallet Balance: {wallet}")
    if wallet < 1:
        print("you dont have sufficient funds")
        break
    else:
        print("Select if Snack(S) or Drink(D)")
        order_type = str(input()).upper()
        if order_type == "S":
            if wallet < 1.00:# if wallet less than snack minimum then print you dont have enough funds
                print("Insufficient Funds")
            else:
                snack()
        elif order_type == "D":
            print("Would you like a Hot(H) or a Cold(C) beverage?")
            drink_type = str(input()).upper()
            if drink_type == "H":
                if wallet < 1.50:
                    print("Insufficient Funds...")
                else:
                    hot_drinks()
            elif drink_type == "C":
                if wallet < 1.00:
                    print("Insufficient Funds")
                else:
                    cold_drinks()
            else:
                print("Sorry, that is Invalid")
        else:
            print("Sorry, that is Invalid")
        print("Would you like to continue? Yes(Y) No (N)")
        command = str(input()).upper()
        if command == "N":
            break
    

print(f"your change is ${wallet}\ndispensing change...\n Thank you for using our vending Machine! Come again soon!")
