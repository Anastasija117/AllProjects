import random
import time

import Linventory


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.regen = 3
        self.inventory = Linventory.Inventory()
        self.level = 1
        self.level_up = False
        self.weapon = None
        self.shield = None
        self.damage = 'Shield🛡️'
        self.clothes = []

    def __str__(self):
        return self.name

    def equip_weapon(self):
        if self.inventory.check_weapons():
            wep = input("Which weapon would you like to equip?: ")
            if self.inventory.get_wep(wep):
                self.weapon = wep
                self.damage = self.inventory.weapons.get(wep,0)
                if self.shield:
                    print(f"\n{self.weapon} equipped with damage "
                          f"{self.damage} and a {self.shield} for protection.\n")
                else:
                    print(f"\n{self.weapon} equipped with damage {self.damage}.\n")

    def equip_shield(self):
        for item in self.inventory.items:
            if item == 'Shield🛡️':
                self.shield = item
                print("\nEquipped shield.")

    def equip_clothes(self):
        if self.inventory.check_clothes():
            eq = print("\nWhat would you like to equip?: ")
            if eq in self.inventory.myclothes:
                self.clothes.append(eq)

        print(f"Equipped clothes: {self.clothes}")




class Animals:
    def __init__(self, player, key=None):
        self.player = player
        self.animals = {"bear":[20,90], "snake":[15,70], "lion":[30,120], "pig":[8,65], "rabid dog":[25,50]}
        self.wep_damage = 0
        self.adamage = 0
        self.animal_health = 0

    def attack(self, animal, react,damage,health):
        outcome = ['You win!',
                   'You lose!']
        action = random.choice(outcome)

        if react == '1':  # Player chooses to attack
            if action == outcome[0]:  # Player wins
                if self.player.weapon:
                    self.wep_damage = self.player.damage
                    print(f"\n{animal}:{health}🩸")
                    print(f"\nYou hit the animal {animal} with {self.player.weapon} "
                          f"and did {self.wep_damage} damage.")
                    time.sleep(1)
                    while health > 0:
                        health = health - self.wep_damage
                        if health < 0:
                            break
                        print("\nHIT")
                        print(f"{animal}:{health}🩸")
                        time.sleep(1)

                    self.player.level += 1
                    self.player.level_up = True
                    self.player.health = 100
                    print(f"\nThe animal is dead!Congrats!You leveled up![{self.player.level}]")
                    print("\nBack to full health")
                else:
                    print(f"\n{animal}:{health}🩸")
                    print(f"\nYou hit the animal {animal} with fists "
                          f"and did 10 damage.")
                    time.sleep(1)
                    while health > 0:
                        health = health - 10
                        if health < 0:
                            break
                        print("\nHIT")
                        print(f"{animal}:{health}🩸")
                        time.sleep(1)

                    self.player.level += 1
                    self.player.level_up = True
                    self.player.health = 100
                    print(f"\nThe animal is dead!Congrats!You leveled up![{self.player.level}]")
                    print("\nBack to full health")




            elif action == outcome[1]:
                self.player.health -= damage
                print(f"You couldn't beat the {animal}.You lost {damage} health.")

        elif react == '2':
            if action == outcome[0]:
                print(f"You managed to run away...this time. ")
            elif action == outcome[1]:
                self.player.health -= damage
                print(f"Couldn't run fast enough from {animal}.You lost {damage} health.")

    def see_animal(self):
        animal = random.choice(list(self.animals.keys()))
        self.adamage, self.animal_health = self.animals[animal]
        print(f"\nA/an {animal} jumps from the bushes!")
        react = input("What will you do?: "
                      "\n1.Attack"
                      "\n2.Run away\n")
        if react == '1' or react == '2':
            self.attack(animal, react,self.adamage,self.animal_health)
        else:
            print("Invalid input.")


class Choice:
    def __init__(self, player):
        self.player = player
        self.react = Animals(self.player)
        self.possibilites = ['You have ran into an abandoned house!',
                             'There seems to be a big box on the right.',
                             'There is some noise...']

    def regenerate(self):
        if self.player.level_up:
            self.player.regen = 3
            self.player.level_up = False
        reg = input("\nDo you want to:\n"
                    "1.Eat"
                    "\n2.Sleep\n")

        if reg == '1':
            if self.player.inventory.if_has_food():
                self.player.inventory.check_food()
                food = input("\nWhat will you choose to eat?: ")
                heal = self.player.inventory.food.get(food, 0)

                if heal > 0:
                    self.player.health += heal
                    if self.player.health > 100:
                        self.player.health = 100
                        print(f"You ate {food} and are at max health.")
                    else:
                        print(f"You ate {food} and gained {heal} health.")
                else:
                    print("That food is not available or doesn't provide any health benefits.")

                self.player.inventory.items.remove(food)

        elif reg == '2':
            if self.player.regen == 0:
                print("You don't have any regens left.Wait for level up!")
                return
            if self.player.regen > 0:
                if self.player.health < 100:
                    self.player.health = min(100, self.player.health + 5)
                    self.player.regen -= 1
                    print(f"You slept and regenerated health. Your health is now "
                          f"{self.player.health}. [{self.player.regen} regens left]")
                else:
                    print("Your health is already full!")


    def choice(self, answer):
        if answer.upper() == 'T':
            print("\nYou are taking some steps....\n")
            action = (random.choice(self.possibilites))
            print(action)

            if action in self.possibilites[0:2]:
                item = self.player.inventory.random_item()
                a = input(f"You found a/an {item}.Do you want to add it to your inventory?: ")
                if a.lower() == 'yes':
                    self.player.inventory.add_item(item)


            elif action == self.possibilites[2]:
                self.react.see_animal()


class Game:

    def run(self):
        print("----Hello.Welcome to Explore World!----")
        char = input("\nWould you like to create a character?: ")
        if not char.lower() == 'yes':
            print("Thank you for playing.Goodbye")
            return

        name = input("Input the name for your character: ")
        player = Player(name)

        print(f"\nHello {player}🧍‍♀️.Welcome!\n")
        print("Here is a guide to help you through your game!")
        print("To see this help window press H.")
        print("To see your inventory press I.")
        print("To take a few steps press T.")
        print("To check weapons press W.")
        print("To equip a weapon press E.")
        print("To equip a shield press ES.")
        print("To equip clothes press EC.")
        print("To see equipped weapon press EQ.")
        print("To check food press F.")
        print("To regenerate press B.")
        print("To see level press L.")
        print("\n--------Starting game--------\n")
        time.sleep(3)

        choices = Choice(player)
        print(f"\nPlayer: {player}🧍‍♀️,Health: {player.health}🩸,Level: {player.level}🔢")
        print("\nYou are starting at the beginning of the forest...\n")

        while player.health > 0:
            print(f"\nHealth: {player.health}🩸\n")
            move = input("\n")

            if move.upper() == 'I':
                player.inventory.show_inventory()

            elif move.upper() == 'T':
                choices.choice(move)

            elif move.upper() == 'B':
                choices.regenerate()

            elif move.upper() == 'W':
                player.inventory.check_weapons()

            elif move.upper() == 'F':
                player.inventory.check_food()

            elif move.upper() == 'L':
                print(f"Player: {player}🧍‍,Level: {player.level}🔢")

            elif move.upper() == 'H':
                print("----------------Help----------------")
                print("Inventory ---> I")
                print("Move forward ---> T")
                print("Weapons ---> W")
                print("Food ---> F")
                print("Regenerate ---> B")
                print("Character level ---> L")
                print("Equip a weapon --> E")
                print("Equipped weapon --> Eq")
                print("------------------------------------")

            elif move.upper() == 'E':
                player.equip_weapon()

            elif move.upper() == 'ES':
                player.equip_shield()

            elif move.upper() == 'EQ':
                if player.weapon and player.shield:
                    print(f"Your equipped weapon is {player.weapon} with damage {player.damage}"
                          f" and {player.shield} for protection")
                elif player.weapon:
                    print(f"Your equipped weapon is {player.weapon} with damage {player.damage}")
                else:
                    print("You don't have a weapon in-hand.")

            elif move.upper() == 'EC':
                player.equip_clothes()

        print("You died.You lost the game")



if __name__ == '__main__':
    p = Game()
    p.run()