import random


# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


# Deck class
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        return [self.cards.pop() for _ in range(n)] if len(self.cards) >= n else []


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck, n=1):
        self.hand.extend(deck.draw(n))

    def show_hand(self):
        return f"{self.name}'s hand: {', '.join(map(str, self.hand))}"


# Blackjack Player class
class BlackjackPlayer(Player):
    def hand_value(self):
        value = 0
        aces = 0
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                       'K': 10, 'A': 11}

        for card in self.hand:
            value += card_values[card.rank]
            if card.rank == 'A':
                aces += 1

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value


# Blackjack Game class
class BlackjackGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [BlackjackPlayer(name) for name in player_names]
        self.dealer = BlackjackPlayer("Dealer")

    def deal_initial_cards(self):
        for player in self.players + [self.dealer]:
            player.draw_card(self.deck, 2)

    def player_turn(self, player):
        while player.hand_value() < 21:
            print(player.show_hand(), "Value:", player.hand_value())
            move = input(f"{player.name}, do you want to hit (h) or stand (s)? ")
            if move.lower() == 'h':
                player.draw_card(self.deck, 1)
            else:
                break

    def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            self.dealer.draw_card(self.deck, 1)

    def determine_winner(self):
        dealer_value = self.dealer.hand_value()
        print(self.dealer.show_hand(), "Value:", dealer_value)
        for player in self.players:
            player_value = player.hand_value()
            if player_value > 21:
                print(f"{player.name} busts! Dealer wins.")
            elif dealer_value > 21 or player_value > dealer_value:
                print(f"{player.name} wins!")
            elif player_value < dealer_value:
                print(f"{player.name} loses to the dealer.")
            else:
                print(f"{player.name} ties with the dealer.")

    def start(self):
        self.deal_initial_cards()
        for player in self.players:
            self.player_turn(player)
        self.dealer_turn()
        self.determine_winner()


# Run the game
game = BlackjackGame(["Alice", "Bob"])
game.start()
