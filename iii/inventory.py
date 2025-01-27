import random


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
        print(f"{item} has been added to your inventory!")

    def show_inventory(self):
        if not self.items:
            print("Your inventory is empty!")
        else:
            print("\nYour inventory: ")
            print(",".join(self.items))

    def random_item(self):
        houseitems = ["Coin🪙", "Burger🍔", "Water bottle🥤",
                            "Hat👒", "Jacket🧥", "Shirt👕", "Pants👖",
                            "Shoe👟", "Glove🧤", "Glasses🕶️", "Stick🥍",
                            "A gun🔫", "A backpack🎒", "Knife🗡️"]
        return random.choice(houseitems)




