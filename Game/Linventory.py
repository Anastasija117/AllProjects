import random


class Inventory:
    def __init__(self):
        self.items = []
        self.weapons = {"Knife🔪":20,"Daggers⚔️":33,"Bow🏹":8,"A gun🔫":50,"Sword🗡️":25,"Stick🥍":15,"Cricket bat🏏":20}
        self.shield = None
        self.food = {"Banana🍌":12,"Grapes🍇":14,"Cherries🍒":12,"Strawberries🍓":18,"Cookie🍪":22,"Fries🍟":25,"Patatos🥔":30,"Burger🍔":40,"Pizza🍕":50,"Watermelon🍉":10,"Bread🍞":25,"Doughnut🍩":17}
        self.clothes = ["Shoe👟", "Glove🧤", "Glasses🕶️","Hat👒", "Jacket🧥", "Shirt👕","Pants👖"]
        self.randomitems = ["Coin🪙",'Shield🛡️']
        self.myweapons = []
        self.myfood = []
        self.myclothes = []

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
        houseitems = list(self.weapons.keys()) + list(self.food.keys()) + self.clothes + self.randomitems
        return random.choice(houseitems)

    def check_clothes(self):
        self.myclothes.clear()
        if self.items:
            for item in self.items:
                if item in self.clothes:
                    self.myclothes.append(item)
            if self.myclothes:
                print(f"\nYour clothes: {','.join(self.myclothes)}")
                return True
            else:
                print("\nYou don't have any clothes in your inventory.")
        else:
            print("\nYour inventory is empty.")

    def check_weapons(self):
        self.myweapons.clear()
        for item in self.items:
            if item in self.weapons:
                self.myweapons.append(item)

        if self.myweapons:
            print(f"Your weapons: {','.join(self.myweapons)}")
            return True
        else:
            print("You have no weapons in your inventory.")

    def get_wep(self,weapon):
        self.myweapons.clear()
        for item in self.items:
            if item in self.weapons:
                self.myweapons.append(item)

        if weapon in self.myweapons:
            return True

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


