
inventory_data ={}

def style1():
    print("\n")
    print("*" * 60)

def style2():
    print("\n")
    print("-" * 60)
def style3():
    print("#" *60)
def add_item():
    style2()
    print("--- Add Item ---")
    item = input("Item Name: ")
    price = float(input("Item Price: "))
    stock = int(input("Item Stock: "))
    category = input("Item Category: ")
    inventory_data[item] = {"price": price, "stock": stock, "category": category}
    print(inventory_data)

#  --- Add or remove stock funtions
def add_stock():
    style2()
    print("--- Add Stock ---")
    item = input("Item Name: ")
    if item in inventory_data:
        stock = int(input("Enter stock quantity: "))
        inventory_data[item]["stock"] += stock
        print(f"Stock added to {item}")
    else:
        print(f"Item '{item}' not found!")

def remove_stock():
    style2()
    print("--- Remove Stock ---")
    item = input("Item Name: ")
    if item in inventory_data:
        stock = int(input("Enter stock quantity: "))
        if inventory_data[item]["stock"] >= stock:
            inventory_data[item]["stock"] -= stock
            print(f"Stock removed from {item}")
        else:
            print(f"Not enough stock to remove from {item}")
    else:
        print(f"Item '{item}' not found!")

# --- Function to Search by category
def search_category():
    style2()
    print("--- Search by Category ---")
    category = input("Enter category: ")
    found_items = [item for item, data in inventory_data.items() if data["category"] == category]
    if found_items:
        print(f"Items in category '{category}': {found_items}")
    else:
        print(f"No items found in category '{category}'")

# --- Function to check stocks
def check_stocks():
    style2()
    print("--- Check Low Stock Items ---")
    low_stock_items = [item for item, data in inventory_data.items() if data["stock"] <= 5]
    if low_stock_items:
        print(f"Low stock items: {low_stock_items}")
    else:
        print("No low stock items found.")


# --- Function to calculate total Inventory
def calculate_total_inventory():
    style2()
    print("--- Total Inventory ---")
    total_value = sum(data["price"] * data["stock"] for data in inventory_data.values())
    print(f"Total inventory value: ${total_value:.2f}")





while(True):
    try:
        style1()
        print("=== SMART INVENTORY MANAGER ===")
        userInput=int(input("= MENU =\n1. Add New Item\n2. Update stock (add/remove)\n3. Search items by category\n4. Check low stock items (≤5 units)\n5. Calculate total inventory value\n6. Exit\nEnter Choice: "))
        if userInput == 1:
            add_item()
        elif userInput == 2:
            while(True):
                try:
                    style2()
                    print("= STOCK MENU =")
                    userInput=int(input("1. Add Stock\n2. Remove Stock\n3. Exit\nEnter Choice: "))
                    if userInput ==1:
                        add_stock()
                    elif userInput == 2:
                        remove_stock()
                    elif userInput == 3:
                        break
                    else:
                        print("Please Choose from available options (1 -3)")
                except ValueError:
                        style3()
                        print("Please Enter valid Input (Only Intergers)")
                        style3()

        elif userInput == 3:
            search_category()
        elif userInput == 4:
            check_stocks()
        elif userInput == 5:
            calculate_total_inventory()
        elif userInput == 6:
            break
        else:
            style3()
            print("Please Choose form available options (1-6)")
            style3()
    except ValueError:
        style3()
        print("Please Enter valid Input (Only Intergers)")
        style3()

