inventory = []

def add_item(list,item):
    if item not in list:
        list.append(item)
    else:
        print(f"Item {item} is already in list!")
def remove_item(list,item):
    if item in list:
        list.remove(item)
    else:
        print(f"Item {item} is not in list!")
def display_inventory(list):
    print(list)
def check_item(list,item):
    return item in list
running = True
while running:
    print("\nSelect an option: "
          "\n1.Add item"
          "\n2.Remove item"
          "\n3.Display inventory"
          "\n4.Check if item exists"
          "\nq.Quit")
    print()
    user_choice = input("Enter your choice: ").lower()
    print()
    if user_choice == "q":
        print("Exiting program.")
        running = False
    elif user_choice == "1":
        item_add = input("Enter an item to add: ")
        add_item(inventory,item_add)
    elif user_choice == "2":
        item_remove = input("Enter an item to remove: ")
        remove_item(inventory,item_remove)
    elif user_choice == "3":
        print("Your inventory: ")
        display_inventory(inventory)
    elif user_choice == "4":
        item_check = input("Enter an item to check: ")
        if check_item(inventory,item_check):
            print(f"Item {item_check} exists in the inventory.")
        else:
            print(f"Item {item_check} doesn't exist in the inventory.")

    else:
        print("Invalid choice.Please try again!")

input("THE END")