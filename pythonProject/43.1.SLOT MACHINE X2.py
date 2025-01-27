# Python slot machine
import random


def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row,row2,row3,bet):
    if row[0] == row[2] == row2[1] == row3[0] == row3[2]:
        print("***JACKPOT***")
        return bet * 100
    elif row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    elif row2[0] == row2[1] == row2[2]:
        if row2[0] == "🍒":
            return bet * 3
        elif row2[0] == "🍉":
            return bet * 4
        elif row2[0] == "🍋":
            return bet * 5
        elif row2[0] == "🔔":
            return bet * 10
        elif row2[0] == "⭐":
            return bet * 20
    elif row3[0] == row3[1] == row3[2]:
        if row3[0] == "🍒":
            return bet * 3
        elif row3[0] == "🍉":
            return bet * 4
        elif row3[0] == "🍋":
            return bet * 5
        elif row3[0] == "🔔":
            return bet * 10
        elif row3[0] == "⭐":
            return bet * 20
    elif row[0] == row2[0] == row3[0]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    elif row[1] == row2[1] == row3[1]:
        if row[1] == "🍒":
            return bet * 3
        elif row[1] == "🍉":
            return bet * 4
        elif row[1] == "🍋":
            return bet * 5
        elif row[1] == "🔔":
            return bet * 10
        elif row[1] == "⭐":
            return bet * 20
    elif row[2] == row2[2] == row3[2]:
        if row[2] == "🍒":
            return bet * 3
        elif row[2] == "🍉":
            return bet * 4
        elif row[2] == "🍋":
            return bet * 5
        elif row[2] == "🔔":
            return bet * 10
        elif row[2] == "⭐":
            return bet * 20
    return 0
def main():
    balance = 100

    print("***********************")
    print("Welcome to PyThon Slots")
    print("Symbols:🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount(q to quit): ")

        if bet == "q":
            break
        elif not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0!")
            continue

        balance -= bet
        row = spin_row()
        row2 = spin_row()
        row3 = spin_row()
        print("Spinning...\n")
        print_row(row)
        print_row(row2)
        print_row(row3)

        payout = get_payout(row,row2,row3,bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout
if __name__ == '__main__':
    main()
