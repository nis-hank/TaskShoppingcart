items = [
    ['Bread', 40],
    ['Cookies', 80],
    ['Butter', 120],
    ['Cheese', 180],
    ['Yoghurt', 60]
]

cart = []

while True:
    print("\nWhat do you want to do?")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding the items to cart")
    print("Enter 3 for updating the items in cart")
    print("Enter 4 for deleting the items in cart")
    print("Enter 5 for printing the bill")
    print("Enter 6 to exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("\nAvailable items:")
        for item in items:
            print("Name: ", item[0], " Price: ", item[1])
    
    elif choice == 2:
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        
        item_price = None
        for item in items:
            if item[0] == item_name:
                item_price = item[1]
                break
        
        if item_price is not None:
            total_price = item_price * quantity
            cart.append([item_name, quantity, item_price, total_price])
            print("Added ", item_name, " x", quantity, " to cart.")
        else:
            print("Item not found.")
    
    elif choice == 3:
        item_name = input("Which item to be updated: ")
        quantity = int(input("Enter the quantity to be updated: "))
        
        found = False
        for item in cart:
            if item[0] == item_name:
                item[1] = quantity
                item[3] = item[1] * item[2]
                found = True
                print("Updated ", item_name, " to quantity ", quantity)
                break
        
        if not found:
            print(item_name, " not found in the cart.")
    
    elif choice == 4:
        item_name = input("Which item to be removed: ")
        
        found = False
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
                found = True
                print("Removed ", item_name, " from the cart.")
                break
        
        if not found:
            print(item_name, " not found in the cart.")
    
    elif choice == 5:
        print("\nName, Quantity, Price, Total")
        total_amount = 0
        for item in cart:
            print(item[0], ",", item[1], ",", item[2], ",", item[3])
            total_amount += item[3]
        print("Total Amount of Bill: ", total_amount)
    
    elif choice == 6:
        break
    
    else:
        print("Invalid choice, please try again.")
