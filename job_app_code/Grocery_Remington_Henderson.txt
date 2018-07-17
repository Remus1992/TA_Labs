# The Grocery Store by Remington Henderson
# written in Python 3.6.3
#
# Greetings,
#
# I'll try and sum up my methodology for the grocery store app below.
# I generally try to mimic real life as best as I can when coding even
# if it doesn't account for the fastest computational time. My reason for
# this more deals with that I would like to work with AI one day and my
# impression is that artificial cognitive thought should follow reality
# more than simplicity (if that makes any sense).
#
# So, in the context of this project, it would've been a lot easier to have made
# a grocery object and then just allow the user to grab that object and put it in
# his/ her cart. I decided instead to create an object which accounted for the total
# inventory of an item in the store. For example, I made it that there was a maximum 50 apples
# and so if a person requested 51, the code would shoot back that there were not enough
# apples in inventory for this request. This equated ultimately to me "copying" the
# contents of an object and creating a new one which would go into cart itself (since
# "splitting" an object is not possible).
#
# I also wanted to add a bit more authenticity to the store by creating aisles and subcategorizing
# the objects to a given aisle. This way, one wouldn't see all the items in the store at once
# but instead see all of the available groceries in a given aisle at a time.
#
# Other than that, the app works as one would expect: adding, removing, clearing the cart,
# viewing the cart (and sorting) all work. The difference comes down to the checkout methods.
#
# I wanted to include for cash and credit options. I implemented two separate bits of code
# I had already written: one for giving change back when purchasing an item and the other
# to check if a credit card number is valid. The method for the later doesn't work for every
# card. It is based on the Luhn Algorithm. In the code, I have a print line which offers up
# for example a working number. You are free to try one of yours yourself. Out of four of
# my credit cards, one of them did actually work which was pretty cool (note: it is not the
# sample one in case you were wondering.)

class Grocery:
    def __init__(self, item_name, aisle_name, price_method, amount_available, price_per_unit):
        self.name = item_name
        self.aisle = aisle_name
        self.separation_method = price_method
        self.available_amount = amount_available
        self.ppu = price_per_unit


class GroceryStore:
    def __init__(self, groceries_list=None):
        self.groceries_list = groceries_list or {}
        self.aisle_dictionary = None
        self.user_cart = []

    def aisle_separation(self):
        # for UPC in self.groceries_list:
        #     print(self.groceries_list[UPC].aisle)
        aisle_list = []
        for UPC in self.groceries_list:
            if self.groceries_list[UPC].aisle not in aisle_list:
                aisle_list.append(self.groceries_list[UPC].aisle)
        # print(aisle_list)

        aisle_dict = {}
        produce_list = []
        toiletries_list = []
        meat_list = []
        cheese_list = []
        bread_list = []

        for UPC in self.groceries_list:
            for i in range(len(aisle_list)):
                if self.groceries_list[UPC].aisle == aisle_list[i]:
                    if aisle_list[i] in "Produce":
                        # aisle_dict[aisle_list[i]] = produce_list.append('hello')
                        produce_list.append({"UPC": UPC, "Name": self.groceries_list[UPC].name,
                                             "Separation_Method": self.groceries_list[UPC].separation_method,
                                             "Available_Amount": self.groceries_list[UPC].available_amount,
                                             "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Toiletries":
                        toiletries_list.append({"UPC": UPC, "Name": self.groceries_list[UPC].name,
                                                "Separation_Method": self.groceries_list[UPC].separation_method,
                                                "Available_Amount": self.groceries_list[UPC].available_amount,
                                                "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Meat":
                        meat_list.append({"UPC": UPC, "Name": self.groceries_list[UPC].name,
                                          "Separation_Method": self.groceries_list[UPC].separation_method,
                                          "Available_Amount": self.groceries_list[UPC].available_amount,
                                          "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Cheese":
                        cheese_list.append({"UPC": UPC, "Name": self.groceries_list[UPC].name,
                                            "Separation_Method": self.groceries_list[UPC].separation_method,
                                            "Available_Amount": self.groceries_list[UPC].available_amount,
                                            "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Bread":
                        bread_list.append({"UPC": UPC, "Name": self.groceries_list[UPC].name,
                                           "Separation_Method": self.groceries_list[UPC].separation_method,
                                           "Available_Amount": self.groceries_list[UPC].available_amount,
                                           "PPU": self.groceries_list[UPC].ppu})
        # print(produce_list)
        # print(toiletries_list)
        # print(meat_list)
        # print(cheese_list)
        # print(bread_list)

        aisle_dict["Produce"] = produce_list
        aisle_dict["Toiletries"] = toiletries_list
        aisle_dict["Meat"] = meat_list
        aisle_dict["Cheese"] = cheese_list
        aisle_dict["Bread"] = bread_list
        # print(aisle_dict)
        self.aisle_dictionary = aisle_dict

    def view_aisle(self, p):
        prompt = p
        print("UPC\t\t{:<15}\t\tAvail.\t\tPrice".format("Name"))
        print("**********************************************************")
        for aisle in self.aisle_dictionary:
            if aisle == prompt:
                # print(self.aisle_dictionary[aisle])
                for item in range(len(self.aisle_dictionary[aisle])):
                    if self.aisle_dictionary[aisle][item]["Separation_Method"] == "buy_by_weight":
                        separation_method = "per pound"
                        print("{:<3}\t\t{:<15}\t\t{:<4}\t\t{:<4}\t\t{:<15}".format(
                            self.aisle_dictionary[aisle][item]["UPC"],
                            self.aisle_dictionary[aisle][item]["Name"],
                            self.aisle_dictionary[aisle][item][
                                "Available_Amount"],
                            self.aisle_dictionary[aisle][item]["PPU"],
                            separation_method))
                    elif self.aisle_dictionary[aisle][item][
                        "Separation_Method"] == "buy_by_amount" and aisle == "Bread":
                        separation_method = "per bag"
                        print("{:<3}\t\t{:<15}\t\t{:<4}\t\t{:<4}\t\t{:<15}".format(
                            self.aisle_dictionary[aisle][item]["UPC"],
                            self.aisle_dictionary[aisle][item]["Name"],
                            self.aisle_dictionary[aisle][item][
                                "Available_Amount"],
                            self.aisle_dictionary[aisle][item]["PPU"],
                            separation_method))
                    else:
                        separation_method = "per package"
                        print("{:<3}\t\t{:<15}\t\t{:<4}\t\t{:<4}\t\t{:<15}".format(
                            self.aisle_dictionary[aisle][item]["UPC"],
                            self.aisle_dictionary[aisle][item]["Name"],
                            self.aisle_dictionary[aisle][item][
                                "Available_Amount"],
                            self.aisle_dictionary[aisle][item]["PPU"],
                            separation_method))

    def add_to_cart(self, p):
        prompt = p
        for aisle in self.aisle_dictionary:
            for item in range(len(self.aisle_dictionary[aisle])):
                if prompt == self.aisle_dictionary[aisle][item]["UPC"]:
                    if self.aisle_dictionary[aisle][item]["Separation_Method"] == "buy_by_weight":
                        weight_amount = float(input(
                            "How many pounds of %s would you like?: " % self.aisle_dictionary[aisle][item]["Name"]))
                        if self.groceries_list[prompt].available_amount - weight_amount > 0:
                            item_amount = weight_amount * self.aisle_dictionary[aisle][item]["PPU"]
                            self.user_cart.append(
                                {str(prompt): {"UPC": prompt, "Name": self.groceries_list[prompt].name,
                                               "Separation_Method": self.groceries_list[prompt].separation_method,
                                               "Purchase_Amount": weight_amount,
                                               "PPU": self.groceries_list[prompt].ppu,
                                               "Item Amount": item_amount}})
                        else:
                            print("Sorry, the store doesn't have that many in stock. Pick a smaller amount")

                    elif self.aisle_dictionary[aisle][item]["Separation_Method"] == "buy_by_amount":
                        amount = float(input("How much %s do you want?: " % self.aisle_dictionary[aisle][item]["Name"]))
                        if self.groceries_list[prompt].available_amount - amount > 0:
                            item_amount = amount * self.aisle_dictionary[aisle][item]["PPU"]
                            self.user_cart.append(
                                {str(prompt): {"UPC": prompt, "Name": self.groceries_list[prompt].name,
                                               "Separation_Method": self.groceries_list[prompt].separation_method,
                                               "Purchase_Amount": amount,
                                               "PPU": self.groceries_list[prompt].ppu,
                                               "Item Amount": item_amount}})
                        else:
                            print("Sorry, the store doesn't have that many in stock. Pick a smaller amount")
        print("**********User Cart**********")
        print("UPC\t\t{:<15}\t{:<7}\t{}".format("NAME", "AMOUNT", "ITEM SUBTOTAL"))
        for item in range(len(self.user_cart)):
            for UPC in self.user_cart[item]:
                print(
                    "{}\t\t{:<15}\t{:<8}{}".format(self.user_cart[item][UPC]["UPC"], self.user_cart[item][UPC]["Name"],
                                                   self.user_cart[item][UPC]["Purchase_Amount"],
                                                   self.user_cart[item][UPC]["Item Amount"]))
        total_cost = 0
        for item in range(len(self.user_cart)):
            for UPC in self.user_cart[item]:
                total_cost += self.user_cart[item][UPC]["Item Amount"]
        print("------------------->Total Cost: %s" % total_cost)

    def clear_cart(self):
        self.user_cart = []

    def remove_from_cart(self, prompt):
        # print(self.user_cart)
        for item in range(len(self.user_cart)):
            if prompt in self.user_cart[item]:
                del self.user_cart[item]
                break
            else:
                pass

    def view_cart(self, prompt):
        if prompt == "subtotal":
            print("UPC\t\t{:<15}\t{:<7}\t{}".format("NAME", "AMOUNT", "ITEM SUBTOTAL"))
            # print(self.user_cart)
            order = sorted(self.user_cart, key=lambda i: list(i.values())[0]['Item Amount'])
            for i in order:
                for k, v in i.items():
                    # print(v['Name'])
                    # print(v['Item Amount'])
                    print("{}\t\t{:<15}\t{:<8}{}".format(v["UPC"], v["Name"], v["Purchase_Amount"], v["Item Amount"]))
            total_cost = 0
            for item in range(len(self.user_cart)):
                for UPC in self.user_cart[item]:
                    total_cost += self.user_cart[item][UPC]["Item Amount"]
            print("Total Cost: %s" % total_cost)
        elif prompt == "name":
            print("UPC\t\t{:<15}\t{:<7}\t{}".format("NAME", "AMOUNT", "ITEM SUBTOTAL"))
            order = sorted(self.user_cart, key=lambda i: list(i.values())[0]['Name'])
            for i in order:
                for k, v in i.items():
                    print("{}\t\t{:<15}\t{:<8}{}".format(v["UPC"], v["Name"], v["Purchase_Amount"], v["Item Amount"]))
            total_cost = 0
            for item in range(len(self.user_cart)):
                for UPC in self.user_cart[item]:
                    total_cost += self.user_cart[item][UPC]["Item Amount"]
            print("Total Cost: %s" % total_cost)

    def change_return(self, cash_given, cost_item):
        twenty_dollar = 2000
        ten_dollar = 1000
        five_dollar = 500
        one_dollar = 100
        quarter = 25
        dime = 10
        nickel = 5
        penny = 1

        citem = cost_item
        money_given = cash_given
        money_given = int(float(money_given) * 100)
        # print(money_given)
        citem = int(float(citem) * 100)
        # print(citem)
        money_back = money_given - citem
        # print(money_back)

        twenty_mb = money_back // twenty_dollar
        partial_total = money_back - twenty_mb * twenty_dollar
        ten_mb = partial_total // ten_dollar
        ten_partial_total = partial_total - ten_mb * ten_dollar
        five_mb = ten_partial_total // five_dollar
        five_partial_total = ten_partial_total - five_mb * five_dollar
        one_mb = five_partial_total // one_dollar
        one_partial_total = five_partial_total - one_mb * one_dollar
        qmb = one_partial_total // quarter
        qpartial_total = one_partial_total - qmb * quarter
        dmb = qpartial_total // dime
        dpartial_total = qpartial_total - dmb * dime
        nmb = dpartial_total // nickel
        npartial_total = dpartial_total - nmb * nickel
        pmb = npartial_total // penny
        ppartial_total = npartial_total - pmb * penny

        print(
            "You need %s 20-dollar bills, %s 10-dollar bills, %s 5-dollar bills, %s 1-dollar bills, %s quarters, %s dimes, %s nickels, %s pennies." % (
                twenty_mb, ten_mb, five_mb, one_mb, qmb, dmb, nmb, pmb))

    def validate_credit_card(self, cc_num):
        # converts string to a list of integers
        list_card_int = list(map(int, list(cc_num)))
        # removes final digit for later verification
        final_value = list_card_int[-1]
        list_card_int.pop()
        # reverses list
        reversed_list = list(reversed(list_card_int))
        # doubles every other item
        for x in range(len(reversed_list)):
            if x % 2 == 0:
                reversed_list[x] *= 2
        doubled = reversed_list
        # subtracts 9 from every number greater than 9
        for x in range(len(doubled)):
            if doubled[x] > 9:
                doubled[x] -= 9
        subtracted_num = doubled
        # takes the sum of all of the numbers in the list
        summed = sum(subtracted_num)
        # converts integer to a string and strips final digit
        str_sd = str(summed)
        str_sd.strip()
        second_num_str = str_sd[-1]
        # converts back to integer
        second_num = int(second_num_str)
        # finally checks the final digit produced with the final digit of the original set of data
        # if they are equal, then the card is a valid CC number according to the Luhn Algorithm
        if final_value == second_num:
            print("Valid Credit Card Number")
            return "Valid"
        else:
            print("Invalid Credit Card Number")
            return "Invalid"

    def store_menu(self):
        while True:
            menu_prompt = input(
                "What would you like to do: View Aisles(aisle), Add Item to Cart(add), "
                "Remove Item from Cart(remove), Clear Cart(clear), View Cart(cart), Check Out(check out): ")
            if menu_prompt == "aisle":
                print("Aisles: Produce, Meat, Bread, Toiletries, Cheese")
                p = input("What aisle would you like to go down?: ").title()
                self.view_aisle(p)

            elif menu_prompt == "add":
                p = input("What is the UPC of the item you'd like to add?: ")
                self.add_to_cart(p)

            elif menu_prompt == "remove":
                p = input("What is the UPC of the item you'd like to remove?: ")
                self.remove_from_cart(p)

            elif menu_prompt == "clear":
                self.clear_cart()

            elif menu_prompt == "cart":
                p = input("Sort by item subtotal (subtotal) or item name (name)?: ")
                self.view_cart(p)

            elif menu_prompt == "check out":
                p = input("Will you be paying with cash (cash) or credit (credit)?: ")
                if p == "cash":
                    while True:
                        cash = int(input("How much will you be giving?: "))
                        total_cost = 0
                        for item in range(len(self.user_cart)):
                            for UPC in self.user_cart[item]:
                                total_cost += self.user_cart[item][UPC]["Item Amount"]
                        if cash - total_cost >= 0:
                            self.change_return(cash, total_cost)
                            return False
                        elif cash - total_cost < 0:
                            print("Insufficient funds")
                            return False
                        else:
                            print("Invalid response")
                            return False
                elif p == "credit":
                    print("Working sample CC#: 4556737586899855")
                    card_number = input("Enter credit card number: ")
                    val_test = self.validate_credit_card(card_number)
                    if val_test == "Valid":
                        print("Have a nice day.")
                    elif val_test == "Invalid":
                        print("Sorry can't complete transaction")
            else:
                print("Not a valid option.")
                print("Please use 'Add' or 'Remove' or 'Cart' or 'Check Out'.")


groceries = {
    # "UPC #": Grocery("ITEM", "Aisle", "buy by weight or amount", # avail, price per unit)
    "001": Grocery("Apples", "Produce", "buy_by_weight", 50, .50),
    "002": Grocery("Pears", "Produce", "buy_by_weight", 60, .45),
    "003": Grocery("Bananas", "Produce", "buy_by_weight", 30, .25),
    "004": Grocery("Cucumbers", "Produce", "buy_by_weight", 100, .30),
    "005": Grocery("Lettuce", "Produce", "buy_by_weight", 200, .15),
    "006": Grocery("Paper Towels", "Toiletries", "buy_by_amount", 30, 3.50),
    "007": Grocery("Toilet Paper", "Toiletries", "buy_by_amount", 50, 2.50),
    "008": Grocery("Toothpaste", "Toiletries", "buy_by_amount", 350, 3.20),
    "009": Grocery("Floss", "Toiletries", "buy_by_amount", 70, 2.50),
    "010": Grocery("Moisturizer", "Toiletries", "buy_by_amount", 52, 2.43),
    "011": Grocery("Pork", "Meat", "buy_by_weight", 123, 4.50),
    "012": Grocery("Beef", "Meat", "buy_by_weight", 250, 3.15),
    "013": Grocery("Chicken", "Meat", "buy_by_weight", 50, 2.23),
    "014": Grocery("Lamb", "Meat", "buy_by_weight", 40, 6.50),
    "015": Grocery("Cheddar", "Cheese", "buy_by_weight", 98, 5.63),
    "016": Grocery("Pepper Jack", "Cheese", "buy_by_weight", 24, 2.12),
    "017": Grocery("Colby", "Cheese", "buy_by_weight", 35, 1.50),
    "018": Grocery("American", "Cheese", "buy_by_weight", 50, 1.49),
    "019": Grocery("Wheat", "Bread", "buy_by_amount", 80, 2.50),
    "020": Grocery("Rye", "Bread", "buy_by_amount", 50, 3.50),
    "021": Grocery("White", "Bread", "buy_by_amount", 150, 1.50),
}

total_groceries = GroceryStore(groceries)

total_groceries.aisle_separation()

total_groceries.store_menu()
