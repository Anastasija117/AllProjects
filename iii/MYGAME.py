import random
from inventory import Inventory

class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.inventory = Inventory()
        self.level = 1

    def __str__(self):
        return self.name




class Choice:
    def __init__(self,player):
        self.player = player
        self.possibilites = ['You have ran into an abandoned house!',
                             'A bear is trying to attack you!',
                             'A snake is trying to attack you!',
                             'A lion is trying to attack you!',
                             'A pig is trying to attack you!',
                             'A dog is trying to attack you!',
                             'An eagle is trying to attack you!'
                                                          ]

    def attack(self):
        outcome = ['You win!',
                         'You lose!']
        action = random.choice(outcome)
        if action == outcome[0]:
            self.player.level += 1
            print(f"You win!Congrats!You leveled up[{self.player.level}]")
        elif action == outcome[1]:
            self.player.health -= 20
            print(f"You have been attacked.You lost 20 health.")

    def runaway(self):
        outcome = ['You win!',
                         'You lose!']
        action = random.choice(outcome)
        if action == outcome[0]:
            print(f"You managed to run away...this time. ")
        elif action == outcome[1]:
            self.player.health -= 20
            print(f"Couldn't run fast enough.You lost 20 health.")

    def regenerate(self):
        if self.player.health <= 95:
            self.player.health += 5
        elif 95 < self.player.health < 100:
            self.player.health = 100

        print(f"You took a nap and regenerated your health.Your health is now "
              f"at {self.player.health}")

    def choice(self,answer):
        if answer == 'T':
            print("You are taking some steps.What will happen...who knows?")
            action = (random.choice(self.possibilites))
            print(action)

            if action == self.possibilites[0]:
                item = self.player.inventory.random_item()
                a = input(f"You found a/an {item}.Do you want to add it to your inventory?: ")
                if a.lower() == 'yes':
                    self.player.inventory.add_item(item)

            elif action in self.possibilites[1:6]:
                react = input("What will you do?: "
                              "\n1.Attack"
                              "\n2.Run away\n")
                if react == '1':
                    self.attack()
                elif react == '2':
                    self.runaway()



class Game:

    def run(self):
        print("----Hello.Welcome to Explore World!----")
        char = input("\nWould you like to create a character?: ")
        if not char.lower() == 'yes':
            print("Thank you for playing.Goodbye")
            return


        name = input("Input the name for your character: ")
        player = Player(name)

        print(f"\nHello {player}.Welcome!\n")
        print("Here is a guide to help you through your game!")
        print("To see your inventory press I.")
        print("To take a few steps press T.")
        print("To take a nap and gain health press B.")
        print(f"\nYour health is {player.health}")

        choices = Choice(player)
        print("\nYou are starting at the beginning of the forest.\n")
        while player.health > 0:
            print(f"Player: {player},Health: {player.health},Level: {player.level}")
            move = input("\nWhat is your next move?: ")

            if move == 'I':
                player.inventory.show_inventory()

            elif move == 'T':
                choices.choice(move)

            elif move == 'B':
                choices.regenerate()








if __name__ == '__main__':
    p = Game()
    p.run()