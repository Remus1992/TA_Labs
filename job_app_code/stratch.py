# The Grocery Store


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
            print(UPC)
            for i in range(len(aisle_list)):
                if self.groceries_list[UPC].aisle == aisle_list[i]:
                    if aisle_list[i] == "Produce":
                        # aisle_dict[aisle_list[i]] = produce_list.append('hello')
                        produce_list.append({"Name": self.groceries_list[UPC].name,
                                             "Separation_Method": self.groceries_list[UPC].separation_method,
                                             "Available_Amount": self.groceries_list[UPC].available_amount,
                                             "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Toiletries":
                        toiletries_list.append({"Name": self.groceries_list[UPC].name,
                                                "Separation_Method": self.groceries_list[UPC].separation_method,
                                                "Available_Amount": self.groceries_list[UPC].available_amount,
                                                "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Meat":
                        meat_list.append({"Name": self.groceries_list[UPC].name,
                                          "Separation_Method": self.groceries_list[UPC].separation_method,
                                          "Available_Amount": self.groceries_list[UPC].available_amount,
                                          "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Cheese":
                        cheese_list.append({"Name": self.groceries_list[UPC].name,
                                            "Separation_Method": self.groceries_list[UPC].separation_method,
                                            "Available_Amount": self.groceries_list[UPC].available_amount,
                                            "PPU": self.groceries_list[UPC].ppu})
                    elif aisle_list[i] == "Bread":
                        bread_list.append({"Name": self.groceries_list[UPC].name,
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
        print("Name\tAmount Available\tPrice Per Unit\tSeparation Method")
        print("****************************************")
        for aisle in self.aisle_dictionary:
            if aisle == prompt:
                # print(self.aisle_dictionary[aisle])
                for item in range(len(self.aisle_dictionary[aisle])):
                    # print(self.aisle_dictionary[aisle][item]["Name"])
                    print("{}\t\t{}\t\t{}\t\t{}".format(self.aisle_dictionary[aisle][item]["Name"],
                                                        self.aisle_dictionary[aisle][item]["Available_Amount"],
                                                        self.aisle_dictionary[aisle][item]["PPU"],
                                                        self.aisle_dictionary[aisle][item]["Separation_Method"]))

    def print_grocery(self, UPC):
        print(self.groceries_list[UPC].aisle)

    def store_menu(self):
        while True:
            menu_prompt = input(
                "What would you like to do: View Aisles, Add Item to Cart, Remove Item from Cart, View Cart, Check Out:")
            if menu_prompt == "Aisles":
                p = input("What aisle would you like to go down?: ")
                self.view_aisle(p)

            elif menu_prompt == "Add":
                pass

            elif menu_prompt == "Remove":
                pass

            elif menu_prompt == "Cart":
                pass

            elif menu_prompt == "Check Out":
                pass

            else:
                print("Not a valid option.")
                print("Please use 'Add' or 'Remove' or 'Cart' or 'Check Out'.")

class ShoppingCart:
    pass


class Checkout:
    pass


groceries = {
    # "UPC #": Grocery("ITEM", "Aisle", "buy by weight or amount", # avail, price per unit)
    "001": Grocery("Apples", "Produce", "buy_by_weight", 50, .50),
    "002": Grocery("Pears", "Produce", "buy_by_weight", 60, .45),
    "003": Grocery("Bananas", "Produce", "buy_by_weight", 30, .25),
    "004": Grocery("Cucumbers", "Produce", "buy_by_weight", 100, .30),
    "005": Grocery("Lettuce", "Produce", "buy_by_weight", 200, .15),
    "006": Grocery("Paper Towels", "Toiletries", "buy_by_amount", 30, 3.50),
    "007": Grocery("Toilet Paper", "Toiletries", "buy_by_amount", 50, 2.50),
    "008": Grocery("Toothpaste", "Toiletries", "buy_by_amount", 50, .50),
    "009": Grocery("Floss", "Toiletries", "buy_by_amount", 50, .50),
    "010": Grocery("Moisturizer", "Toiletries", "buy_by_amount", 50, .50),
    "011": Grocery("Pork", "Meat", "buy_by_weight", 50, .50),
    "012": Grocery("Beef", "Meat", "buy_by_weight", 50, .50),
    "013": Grocery("Chicken", "Meat", "buy_by_weight", 50, .50),
    "014": Grocery("Lamb", "Meat", "buy_by_weight", 50, .50),
    "015": Grocery("Cheddar", "Cheese", "buy_by_weight", 50, .50),
    "016": Grocery("Pepper Jack", "Cheese", "buy_by_weight", 50, .50),
    "017": Grocery("Colby", "Cheese", "buy_by_weight", 50, .50),
    "018": Grocery("American", "Cheese", "buy_by_weight", 50, .50),
    "019": Grocery("Wheat", "Bread", "buy_by_amount", 50, .50),
    "020": Grocery("Rye", "Bread", "buy_by_amount", 50, .50),
    "021": Grocery("White", "Bread", "buy_by_amount", 50, .50),
}

total_groceries = GroceryStore(groceries)

total_groceries.aisle_separation()
# total_groceries.view_aisle()
total_groceries.store_menu()
# total_groceries.print_grocery("021")

#
