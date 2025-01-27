# Python banking program
def show_balance(balance):
    print("*************************")
    print(f"Your balance is ${balance:.2f}")
    print("*************************")
    print()

def deposit():
    print("*************************")
    amount = float(input("Enter the amount you want to deposit: "))
    print("*************************")
    print()
    if amount < 0:
        print("*************************")
        print("That is not a valid amount!")
        print("*************************")
        print()
        return 0
    else:
        return amount

def withdraw(balance):
    print("*************************")
    amount = float(input("Enter the amount you want to withdrawn: "))
    print("*************************")
    print()
    if amount > balance:
        print("*************************")
        print("Insufficient funds")
        print("*************************")
        print()
        return 0
    elif amount < 0:
        print("*************************")
        print("Amount must be greater than 0")
        print("*************************")
        print()
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True


    while is_running:
        print("*************************")
        print("     Banking program   ")
        print("      1.Show balance    ")
        print("       2.Deposit   ")
        print("       3.Withdraw  ")
        print("        4.Exit         ")
        print("*************************")
        print()
        print("*************************")
        choice = input("Enter your choice(1-4): ")
        print("*************************")
        print()
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*************************")
            print("That is not a valid choice!")
            print("*************************")

    print("*************************")
    print("Thank you! Have a nice day!")
    print("*************************")

if __name__ == '__main__':
    main()