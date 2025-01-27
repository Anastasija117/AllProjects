
import random
class Dice:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll(self,count=6):
        return [random.randint(1,self.sides) for _ in range(count)]


class Player:
    def __init__(self,name):
        self.name = name
        self.scores = {
            "Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
            "3 of a Kind": 0, "4 of a Kind": 0, "Full House": 0, "Small Straight": 0,
            "Large Straight": 0, "Yahtzee": 0, "Chance": 0
        }
    def update_score(self,category,value):
        if category in self.scores and self.scores[category] == 0:
            self.scores[category] = value
        else:
            print("Invalid or already chosen category.Try again")

    def total_score(self):
        return sum(self.scores.values())
    def display_score(self):
        pass

class YatzeeGame:
    def __init__(self,players):
        self.dice = Dice()
        self.players = [Player(name.strip()) for name in players]

    def play_round(self,player):
        print(f"🎲{player.name} turn🎲",end= " ")
    def play(self):
        pass



player_names = input("Enter your players names(comma seperated): ").split(",")
print(player_names)
dice = Dice()
print(dice.roll())

