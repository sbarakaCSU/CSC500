# Creating ItemToPurchase class
class ItemToPurchase:
    #Initializing name, price, quantity, and description
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    #Method to print the cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

    #Method to print the item description
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# ShoppingCart class
class ShoppingCart:

    #Initializes the cart with customer name, date, and an empty list
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #MEthod to add items to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    #Method to remove an item by name from the cart
    def remove_item(self, item_name):
        found = False
        #If name is found
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        #If name is not found
        if not found:
            print("That item is not in the cart")

    #Method to modify an item in the cart (quantity, price, or description)
    def modify_item(self, modifiedItem):
        #If name is found
        found = False
        for item in self.cart_items:
            if item.item_name == modifiedItem.item_name:
                if modifiedItem.item_price != 0:
                    item.item_price = modifiedItem.item_price
                if modifiedItem.item_quantity != 0:
                    item.item_quantity = modifiedItem.item_quantity
                found = True
                break
        #If name is not found
        if not found:
            print("That item is not in the cart")
            
    #Method to calculate and return the total cost of all items in the cart
    def get_num_items_in_cart(self):
        total_quantity = sum([item.item_quantity for item in self.cart_items])
        return total_quantity

    #Method to print the total cost and details of the items in the cart
    def get_cost_of_cart(self):
        total_cost = sum([item.item_price * item.item_quantity for item in self.cart_items])
        return total_cost

    #Method to print the description of each item in the cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    #Method to print the description of each item in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

# print_menu function
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option: "
    )
    option = ""
    while option != "q":
        print(menu)
        option = input()
        if option == "a":
            #Add item
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
        elif option == "r":
            #Remove item
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)
        elif option == "c":
            #Modify item quantity
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))
            modified_item = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            cart.modify_item(modified_item)
        elif option == "i":
            #Output item descriptions
            cart.print_descriptions()
        elif option == "o":
            #Output shopping cart
            cart.print_total()
        elif option != "q":
            print("Invalid option, please try again.")

def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print_menu(cart)



if __name__ == "__main__":
    main()
