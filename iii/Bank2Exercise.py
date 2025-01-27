
class BankAcc:
    def __init__(self,ID,name,balance=0.0,pin=0000):
        self.ID = ID
        self.name = name
        self.balance = balance
        self.transactions = []
        self.pin = pin


    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transactions("Deposit",amount))
            print(f"\nDeposited ${amount} to {self.name}.New balance is ${self.balance}.")
            print()
        else:
            print("\nDeposit must be greater than 0!")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transactions("Withdraw",amount))
            print(f"\nWithdrawn ${amount} from {self.name}.New balance ${self.balance}")
            print()
        else:
            print("\nInvalid withdrawal or insufficient funds.\n")

    def check_balance(self):
        print()
        print(f"Account ID: {self.ID}, Name: {self.name}, Balance: ${self.balance}")
        print()
    def s_transactions(self):
        if not self.transactions:
            print(f"\nThere haven't been any transactions for {self.name}.")
        else:
            print(f"\nTransaction history for {self.name}")
            for tr in self.transactions:
                print(f"\n{tr.type}:{tr.amount:.2f}")

    def check_pin(self):
        attempt = 3
        while attempt > 0:
            pin = input("Enter your pin: ")
            if pin == self.pin:
                print("\nCorrect pin.Loading...\n")
                return True
            else:
                attempt -= 1
                print(f"Incorrect PIN!{attempt} attempt(s) left.")

        print("\nToo many incorrect attempts! Access denied!")
        return False



class Transactions:
    def __init__(self,type,amount):
        self.type = type
        self.amount = amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_acc(self):
        id = input("\nEnter your account number: ")
        if id in self.accounts:
            print("\nThat account already exists!")
            return
        name = input("Enter your account holder's name: ")
        balance = float(input("Enter your initial balance: "))
        pin = input("Input your pin: ")

        self.accounts[id]=BankAcc(id,name,balance,pin)
        print()
        print(f"Account created successfully for {name}!")
        print()

    def get_acc(self):
        acc = input("\nEnter your account number: ")
        return self.accounts.get(acc, None)

    def display_accs(self):
        if not self.accounts:
            print("There are no accounts!")
            return

        print()
        print("---------------Bank accounts---------------")
        for accid,name in self.accounts.items():
            print(f"ID Number: {accid}, Account Name: {name.name}")
        print("-------------------------------------------")
        print()

    def run(self):
        while True:
            print("--------BANK SYSTEM MENU--------")
            print("       1.Create account")
            print("        2.Deposit money")
            print("       3.Withdraw money")
            print("        4.Check balance")
            print("      5.View transactions")
            print("        6.Show accounts")
            print("             7.Exit")
            print("--------------------------------")

            choice = input("Choose an option:")

            if choice == "1":
                self.create_acc()

            elif choice in ["2","3","4","5"]:
                account = self.get_acc()
                if not account:
                    print("\nAccount not found.Try again!\n")
                    continue
                if account.check_pin():
                    if choice == "2":
                        amount = float(input("Enter the amount you want to deposit: "))
                        account.deposit(amount)

                    elif choice == "3":
                        amount = float(input("Enter the amount you want to withdraw: "))
                        account.withdraw(amount)

                    elif choice == "4":
                        account.check_balance()

                    elif choice == "5":
                        account.s_transactions()

            elif choice == "6":
                self.display_accs()

            elif choice == "7":
                print("\nThanks for using our bank system!See you next time!")
                break
            else:
                pass

if __name__ == '__main__':
    bank = Bank()
    bank.run()