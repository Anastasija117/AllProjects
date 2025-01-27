import random


class Inventory:
    def __init__(self):
        self.items = []
        self.weapons = {"A gun🔫":40,"Knife🗡️":25,"Stick🥍":15}
        self.food = {"Burger🍔":25,"Pizza🍕":20,"Watermelon🍉":10,"Bread🍞":15,"Doughnut🍩":17}
        self.myweapons = []
        self.myfood = []

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
        houseitems = ["Coin🪙", "Burger🍔", "Pizza🍕","Water bottle🥤",
                            "Hat👒", "Jacket🧥", "Shirt👕", "Pants👖",
                            "Shoe👟", "Glove🧤", "Glasses🕶️","Bread🍞", "Stick🥍",
                            "A gun🔫", "A backpack🎒", "Knife🗡️","Watermelon🍉",
                      "Doughnut🍩"]
        return random.choice(houseitems)



    def check_weapons(self):
        self.myweapons.clear()
        for item in self.items:
            if item in self.weapons:
                self.myweapons.append(item)

        if self.myweapons:
            print(f"Your weapons: {','.join(self.myweapons)}")
        else:
            print("You have no weapons in your inventory.")

    def if_has_food(self):
        self.myfood.clear()
        for item in self.items:
            if item in self.food:
                self.myfood.append(item)
                return True
        print(f"There isn't any food in your inventory.")
        return False

    def check_food(self):
        self.myfood.clear()
        for item in self.items:
            if item in self.food:
                self.myfood.append(item)

        if self.myfood:
            print(f"Your food: {','.join(self.myfood)}")
            return True
        else:
            print(f"There isn't any food in your inventory.")
            return False


